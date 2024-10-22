"""Type checking code for statements.

Operates on statements in a basic block after CFG construction. In particular, we
assume that statements involving control flow (i.e. if, while, break, and return
statements) have been removed during CFG construction.

After checking, we return a desugared statement where all sub-expression have been type
annotated.
"""

import ast
from collections.abc import Sequence

from guppylang.ast_util import AstVisitor, with_loc, with_type
from guppylang.cfg.bb import BB, BBStatement
from guppylang.checker.core import Context, FieldAccess, Variable
from guppylang.checker.expr_checker import ExprChecker, ExprSynthesizer
from guppylang.error import GuppyError, GuppyTypeError, InternalGuppyError
from guppylang.nodes import NestedFunctionDef, PlaceNode
from guppylang.tys.parsing import type_from_ast
from guppylang.tys.subst import Subst
from guppylang.tys.ty import NoneType, StructType, TupleType, Type


class StmtChecker(AstVisitor[BBStatement]):
    ctx: Context
    bb: BB | None
    return_ty: Type | None

    def __init__(
        self, ctx: Context, bb: BB | None = None, return_ty: Type | None = None
    ) -> None:
        assert not return_ty or not return_ty.unsolved_vars
        self.ctx = ctx
        self.bb = bb
        self.return_ty = return_ty

    def check_stmts(self, stmts: Sequence[BBStatement]) -> list[BBStatement]:
        return [self.visit(s) for s in stmts]

    def _synth_expr(self, node: ast.expr) -> tuple[ast.expr, Type]:
        return ExprSynthesizer(self.ctx).synthesize(node)

    def _check_expr(
        self, node: ast.expr, ty: Type, kind: str = "expression"
    ) -> tuple[ast.expr, Subst]:
        return ExprChecker(self.ctx).check(node, ty, kind)

    def _check_assign(self, lhs: ast.expr, ty: Type, node: ast.stmt) -> ast.expr:
        """Helper function to check assignments with patterns."""
        match lhs:
            # Easiest case is if the LHS pattern is a single variable.
            case ast.Name(id=x):
                var = Variable(x, ty, lhs)
                self.ctx.locals[x] = var
                return with_loc(lhs, with_type(ty, PlaceNode(place=var)))

            # The LHS could also be a field `expr.field`
            case ast.Attribute(value=value, attr=attr):
                value, struct_ty = self._synth_expr(value)
                if (
                    not isinstance(struct_ty, StructType)
                    or attr not in struct_ty.field_dict
                ):
                    raise GuppyTypeError(
                        f"Expression of type `{struct_ty}` has no attribute `{attr}`",
                        # Unfortunately, `attr` doesn't contain source annotations, so
                        # we have to use `lhs` as the error location
                        lhs,
                    )
                field = struct_ty.field_dict[attr]
                # TODO: In the future, we could infer some type args here
                if field.ty != ty:
                    raise GuppyTypeError(
                        f"Cannot assign expression of type `{ty}` to field with type "
                        f"`{field.ty}`",
                        lhs,
                    )
                if not isinstance(value, PlaceNode):
                    # For now we complain if someone tries to assign to something that
                    # is not a place, e.g. `f().a = 4`. This would only make sense if
                    # there is another reference to the return value of `f`, otherwise
                    # the mutation cannot be observed. We can start supporting this once
                    # we have proper reference semantics.
                    raise GuppyError(
                        "Assigning to this expression is not supported yet. Consider "
                        "binding the expression to variable and mutate that variable "
                        "instead.",
                        value,
                    )
                if not field.ty.linear:
                    raise GuppyError(
                        "Mutation of classical fields is not supported yet", lhs
                    )
                place = FieldAccess(value.place, struct_ty.field_dict[attr], lhs)
                return with_loc(lhs, with_type(ty, PlaceNode(place=place)))

            # The only other thing we support right now are tuples
            case ast.Tuple(elts=elts) as lhs:
                tys = ty.element_types if isinstance(ty, TupleType) else [ty]
                n, m = len(elts), len(tys)
                if n != m:
                    raise GuppyTypeError(
                        f"{'Too many' if n < m else 'Not enough'} values to unpack "
                        f"(expected {n}, got {m})",
                        node,
                    )
                lhs.elts = [
                    self._check_assign(pat, el_ty, node)
                    for pat, el_ty in zip(elts, tys, strict=True)
                ]
                return with_type(ty, lhs)

            # TODO: Python also supports assignments like `[a, b] = [1, 2]` or
            #  `a, *b = ...`. The former would require some runtime checks but
            #  the latter should be easier to do (unpack and repack the rest).
            case _:
                raise GuppyError("Assignment pattern not supported", lhs)

    def visit_Assign(self, node: ast.Assign) -> ast.Assign:
        if len(node.targets) > 1:
            # This is the case for assignments like `a = b = 1`
            raise GuppyError("Multi assignment not supported", node)

        [target] = node.targets
        node.value, ty = self._synth_expr(node.value)
        node.targets = [self._check_assign(target, ty, node)]
        return node

    def visit_AnnAssign(self, node: ast.AnnAssign) -> ast.stmt:
        if node.value is None:
            raise GuppyError(
                "Variable declaration is not supported. Assignment is required", node
            )
        ty = type_from_ast(node.annotation, self.ctx.globals)
        node.value, subst = self._check_expr(node.value, ty)
        assert not ty.unsolved_vars  # `ty` must be closed!
        assert len(subst) == 0
        target = self._check_assign(node.target, ty, node)
        return with_loc(node, ast.Assign(targets=[target], value=node.value))

    def visit_AugAssign(self, node: ast.AugAssign) -> ast.stmt:
        bin_op = with_loc(
            node, ast.BinOp(left=node.target, op=node.op, right=node.value)
        )
        assign = with_loc(node, ast.Assign(targets=[node.target], value=bin_op))
        return self.visit_Assign(assign)

    def visit_Expr(self, node: ast.Expr) -> ast.stmt:
        # An expression statement where the return value is discarded
        node.value, ty = self._synth_expr(node.value)
        if ty.linear:
            raise GuppyTypeError(f"Value with linear type `{ty}` is not used", node)
        return node

    def visit_Return(self, node: ast.Return) -> ast.stmt:
        if not self.return_ty:
            raise InternalGuppyError("return_ty required to check return stmt!")

        if node.value is not None:
            node.value, subst = self._check_expr(
                node.value, self.return_ty, "return value"
            )
            assert len(subst) == 0  # `self.return_ty` is closed!
        elif not isinstance(self.return_ty, NoneType):
            raise GuppyTypeError(
                f"Expected return value of type `{self.return_ty}`", None
            )
        return node

    def visit_NestedFunctionDef(self, node: NestedFunctionDef) -> ast.stmt:
        from guppylang.checker.func_checker import check_nested_func_def

        if not self.bb:
            raise InternalGuppyError("BB required to check nested function def!")

        func_def = check_nested_func_def(node, self.bb, self.ctx)
        self.ctx.locals[func_def.name] = Variable(func_def.name, func_def.ty, func_def)
        return func_def

    def visit_If(self, node: ast.If) -> None:
        raise InternalGuppyError("Control-flow statement should not be present here.")

    def visit_While(self, node: ast.While) -> None:
        raise InternalGuppyError("Control-flow statement should not be present here.")

    def visit_Break(self, node: ast.Break) -> None:
        raise InternalGuppyError("Control-flow statement should not be present here.")

    def visit_Continue(self, node: ast.Continue) -> None:
        raise InternalGuppyError("Control-flow statement should not be present here.")
