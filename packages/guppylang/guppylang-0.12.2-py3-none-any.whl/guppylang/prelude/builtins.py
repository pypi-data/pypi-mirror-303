"""Guppy module for builtin types and operations."""

# mypy: disable-error-code="empty-body, misc, override, valid-type, no-untyped-def"

from typing import Any, Generic, TypeVar

import hugr.std.int

from guppylang.decorator import guppy
from guppylang.definition.custom import DefaultCallChecker, NoopCompiler
from guppylang.prelude._internal.checker import (
    ArrayLenChecker,
    CallableChecker,
    CoercingChecker,
    DunderChecker,
    FailingChecker,
    NewArrayChecker,
    ResultChecker,
    ReversingChecker,
    UnsupportedChecker,
)
from guppylang.prelude._internal.compiler.arithmetic import (
    FloatBoolCompiler,
    FloatDivmodCompiler,
    FloatFloordivCompiler,
    FloatModCompiler,
    IFromBoolCompiler,
    IntTruedivCompiler,
    IToBoolCompiler,
    NatTruedivCompiler,
)
from guppylang.prelude._internal.compiler.array import (
    ArrayGetitemCompiler,
    ArraySetitemCompiler,
    NewArrayCompiler,
)
from guppylang.prelude._internal.util import (
    float_op,
    int_op,
    logic_op,
    unsupported_op,
)
from guppylang.tys.builtin import (
    array_type_def,
    bool_type_def,
    float_type_def,
    int_type_def,
    linst_type_def,
    list_type_def,
    nat_type_def,
)

guppy.init_module(import_builtins=False)

T = guppy.type_var("T")
L = guppy.type_var("L", linear=True)


def py(*args: Any) -> Any:
    """Function to tag compile-time evaluated Python expressions in a Guppy context.

    This function acts like the identity when execute in a Python context.
    """
    return tuple(args)


class _Owned:
    """Dummy class to support `@owned` annotations."""

    def __rmatmul__(self, other: Any) -> Any:
        return other


owned = _Owned()


class nat:
    """Class to import in order to use nats."""


_T = TypeVar("_T")
_n = TypeVar("_n")


class array(Generic[_T, _n]):
    """Class to import in order to use arrays."""

    def __init__(self, *args: _T):
        pass


@guppy.extend_type(bool_type_def)
class Bool:
    @guppy.hugr_op(logic_op("And"))
    def __and__(self: bool, other: bool) -> bool: ...

    @guppy.custom(NoopCompiler())
    def __bool__(self: bool) -> bool: ...

    @guppy.hugr_op(logic_op("Eq"))
    def __eq__(self: bool, other: bool) -> bool: ...

    @guppy.custom(IFromBoolCompiler())
    def __int__(self: bool) -> int: ...

    @guppy.custom(IFromBoolCompiler())
    def __nat__(self: bool) -> nat: ...

    @guppy.custom(checker=DunderChecker("__bool__"), higher_order_value=False)
    def __new__(x): ...

    @guppy.hugr_op(logic_op("Or"))
    def __or__(self: bool, other: bool) -> bool: ...

    @guppy.hugr_op(unsupported_op("Xor"))  # TODO: Missing op
    def __xor__(self: bool, other: bool) -> bool: ...


@guppy.extend_type(nat_type_def)
class Nat:
    @guppy.custom(NoopCompiler())
    def __abs__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("iadd"))
    def __add__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("iand"))
    def __and__(self: nat, other: nat) -> nat: ...

    @guppy.custom(IToBoolCompiler())
    def __bool__(self: nat) -> bool: ...

    @guppy.custom(NoopCompiler())
    def __ceil__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("idivmod_u", n_vars=2))
    def __divmod__(self: nat, other: nat) -> tuple[nat, nat]: ...

    @guppy.hugr_op(int_op("ieq"))
    def __eq__(self: nat, other: nat) -> bool: ...

    @guppy.hugr_op(int_op("convert_u", hugr.std.int.CONVERSIONS_EXTENSION))
    def __float__(self: nat) -> float: ...

    @guppy.custom(NoopCompiler())
    def __floor__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("idiv_u"))
    def __floordiv__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ige_u"))
    def __ge__(self: nat, other: nat) -> bool: ...

    @guppy.hugr_op(int_op("igt_u"))
    def __gt__(self: nat, other: nat) -> bool: ...

    @guppy.hugr_op(int_op("iu_to_s"))
    def __int__(self: nat) -> int: ...

    @guppy.hugr_op(int_op("inot"))
    def __invert__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("ile_u"))
    def __le__(self: nat, other: nat) -> bool: ...

    @guppy.hugr_op(int_op("ishl", n_vars=2))
    def __lshift__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ilt_u"))
    def __lt__(self: nat, other: nat) -> bool: ...

    @guppy.hugr_op(int_op("imod_u", n_vars=2))
    def __mod__(self: nat, other: nat) -> int: ...

    @guppy.hugr_op(int_op("imul"))
    def __mul__(self: nat, other: nat) -> nat: ...

    @guppy.custom(NoopCompiler())
    def __nat__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("ine"))
    def __ne__(self: nat, other: nat) -> bool: ...

    @guppy.custom(checker=DunderChecker("__nat__"), higher_order_value=False)
    def __new__(x): ...

    @guppy.hugr_op(int_op("ior"))
    def __or__(self: nat, other: nat) -> nat: ...

    @guppy.custom(NoopCompiler())
    def __pos__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("ipow"))
    def __pow__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("iadd"), ReversingChecker())
    def __radd__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("iand"), ReversingChecker())
    def __rand__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("idivmod_u"), ReversingChecker())
    def __rdivmod__(self: nat, other: nat) -> tuple[nat, nat]: ...

    @guppy.hugr_op(int_op("idiv_u"), ReversingChecker())
    def __rfloordiv__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ishl"), ReversingChecker())
    def __rlshift__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("imod_u"), ReversingChecker())
    def __rmod__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("imul"), ReversingChecker())
    def __rmul__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ior"), ReversingChecker())
    def __ror__(self: nat, other: nat) -> nat: ...

    @guppy.custom(NoopCompiler())
    def __round__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("ipow"), ReversingChecker())
    def __rpow__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ishr"), ReversingChecker())
    def __rrshift__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("ishr"))
    def __rshift__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("isub"), ReversingChecker())
    def __rsub__(self: nat, other: nat) -> nat: ...

    @guppy.custom(NatTruedivCompiler(), ReversingChecker())
    def __rtruediv__(self: nat, other: nat) -> float: ...

    @guppy.hugr_op(int_op("ixor"), ReversingChecker())
    def __rxor__(self: nat, other: nat) -> nat: ...

    @guppy.hugr_op(int_op("isub"))
    def __sub__(self: nat, other: nat) -> nat: ...

    @guppy.custom(NatTruedivCompiler())
    def __truediv__(self: nat, other: nat) -> float: ...

    @guppy.custom(NoopCompiler())
    def __trunc__(self: nat) -> nat: ...

    @guppy.hugr_op(int_op("ixor"))
    def __xor__(self: nat, other: nat) -> nat: ...


@guppy.extend_type(int_type_def)
class Int:
    @guppy.hugr_op(int_op("iabs"))  # TODO: Maybe wrong? (signed vs unsigned!)
    def __abs__(self: int) -> int: ...

    @guppy.hugr_op(int_op("iadd"))
    def __add__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("iand"))
    def __and__(self: int, other: int) -> int: ...

    @guppy.custom(IToBoolCompiler())
    def __bool__(self: int) -> bool: ...

    @guppy.custom(NoopCompiler())
    def __ceil__(self: int) -> int: ...

    @guppy.hugr_op(int_op("idivmod_s"))
    def __divmod__(self: int, other: int) -> tuple[int, int]: ...

    @guppy.hugr_op(int_op("ieq"))
    def __eq__(self: int, other: int) -> bool: ...

    @guppy.hugr_op(int_op("convert_s", hugr.std.int.CONVERSIONS_EXTENSION))
    def __float__(self: int) -> float: ...

    @guppy.custom(NoopCompiler())
    def __floor__(self: int) -> int: ...

    @guppy.hugr_op(int_op("idiv_s"))
    def __floordiv__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ige_s"))
    def __ge__(self: int, other: int) -> bool: ...

    @guppy.hugr_op(int_op("igt_s"))
    def __gt__(self: int, other: int) -> bool: ...

    @guppy.custom(NoopCompiler())
    def __int__(self: int) -> int: ...

    @guppy.hugr_op(int_op("inot"))
    def __invert__(self: int) -> int: ...

    @guppy.hugr_op(int_op("ile_s"))
    def __le__(self: int, other: int) -> bool: ...

    @guppy.hugr_op(int_op("ishl"))  # TODO: RHS is unsigned
    def __lshift__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ilt_s"))
    def __lt__(self: int, other: int) -> bool: ...

    @guppy.hugr_op(int_op("imod_s"))
    def __mod__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("imul"))
    def __mul__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("is_to_u"))  # TODO
    def __nat__(self: int) -> nat: ...

    @guppy.hugr_op(int_op("ine"))
    def __ne__(self: int, other: int) -> bool: ...

    @guppy.hugr_op(int_op("ineg"))
    def __neg__(self: int) -> int: ...

    @guppy.custom(checker=DunderChecker("__int__"), higher_order_value=False)
    def __new__(x): ...

    @guppy.hugr_op(int_op("ior"))
    def __or__(self: int, other: int) -> int: ...

    @guppy.custom(NoopCompiler())
    def __pos__(self: int) -> int: ...

    @guppy.hugr_op(int_op("ipow"))
    def __pow__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("iadd"), ReversingChecker())
    def __radd__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("iand"), ReversingChecker())
    def __rand__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("idivmod_s"), ReversingChecker())
    def __rdivmod__(self: int, other: int) -> tuple[int, int]: ...

    @guppy.hugr_op(int_op("idiv_s"), ReversingChecker())
    def __rfloordiv__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ishl"), ReversingChecker())  # TODO: RHS is unsigned
    def __rlshift__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("imod_s"), ReversingChecker())
    def __rmod__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("imul"), ReversingChecker())
    def __rmul__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ior"), ReversingChecker())
    def __ror__(self: int, other: int) -> int: ...

    @guppy.custom(NoopCompiler())
    def __round__(self: int) -> int: ...

    @guppy.hugr_op(int_op("ipow"), ReversingChecker())
    def __rpow__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ishr"), ReversingChecker())  # TODO: RHS is unsigned
    def __rrshift__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("ishr"))  # TODO: RHS is unsigned
    def __rshift__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("isub"), ReversingChecker())
    def __rsub__(self: int, other: int) -> int: ...

    @guppy.custom(IntTruedivCompiler(), ReversingChecker())
    def __rtruediv__(self: int, other: int) -> float: ...

    @guppy.hugr_op(int_op("ixor"), ReversingChecker())
    def __rxor__(self: int, other: int) -> int: ...

    @guppy.hugr_op(int_op("isub"))
    def __sub__(self: int, other: int) -> int: ...

    @guppy.custom(IntTruedivCompiler())
    def __truediv__(self: int, other: int) -> float: ...

    @guppy.custom(NoopCompiler())
    def __trunc__(self: int) -> int: ...

    @guppy.hugr_op(int_op("ixor"))
    def __xor__(self: int, other: int) -> int: ...


@guppy.extend_type(float_type_def)
class Float:
    @guppy.hugr_op(float_op("fabs"), CoercingChecker())
    def __abs__(self: float) -> float: ...

    @guppy.hugr_op(float_op("fadd"), CoercingChecker())
    def __add__(self: float, other: float) -> float: ...

    @guppy.custom(FloatBoolCompiler(), CoercingChecker())
    def __bool__(self: float) -> bool: ...

    @guppy.hugr_op(float_op("fceil"), CoercingChecker())
    def __ceil__(self: float) -> float: ...

    @guppy.custom(FloatDivmodCompiler(), CoercingChecker())
    def __divmod__(self: float, other: float) -> tuple[float, float]: ...

    @guppy.hugr_op(float_op("feq"), CoercingChecker())
    def __eq__(self: float, other: float) -> bool: ...

    @guppy.custom(NoopCompiler(), CoercingChecker())
    def __float__(self: float) -> float: ...

    @guppy.hugr_op(float_op("ffloor"), CoercingChecker())
    def __floor__(self: float) -> float: ...

    @guppy.custom(FloatFloordivCompiler(), CoercingChecker())
    def __floordiv__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fge"), CoercingChecker())
    def __ge__(self: float, other: float) -> bool: ...

    @guppy.hugr_op(float_op("fgt"), CoercingChecker())
    def __gt__(self: float, other: float) -> bool: ...

    @guppy.hugr_op(
        unsupported_op("trunc_s"), CoercingChecker()
    )  # TODO `trunc_s` returns an option
    def __int__(self: float) -> int: ...

    @guppy.hugr_op(float_op("fle"), CoercingChecker())
    def __le__(self: float, other: float) -> bool: ...

    @guppy.hugr_op(float_op("flt"), CoercingChecker())
    def __lt__(self: float, other: float) -> bool: ...

    @guppy.custom(FloatModCompiler(), CoercingChecker())
    def __mod__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fmul"), CoercingChecker())
    def __mul__(self: float, other: float) -> float: ...

    @guppy.hugr_op(
        unsupported_op("trunc_u"), CoercingChecker()
    )  # TODO `trunc_u` returns an option
    def __nat__(self: float) -> nat: ...

    @guppy.hugr_op(float_op("fne"), CoercingChecker())
    def __ne__(self: float, other: float) -> bool: ...

    @guppy.hugr_op(float_op("fneg"), CoercingChecker())
    def __neg__(self: float) -> float: ...

    @guppy.custom(checker=DunderChecker("__float__"), higher_order_value=False)
    def __new__(x): ...

    @guppy.custom(NoopCompiler(), CoercingChecker())
    def __pos__(self: float) -> float: ...

    @guppy.hugr_op(float_op("fpow"))  # TODO
    def __pow__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fadd"), ReversingChecker(CoercingChecker()))
    def __radd__(self: float, other: float) -> float: ...

    @guppy.custom(FloatDivmodCompiler(), ReversingChecker(CoercingChecker()))
    def __rdivmod__(self: float, other: float) -> tuple[float, float]: ...

    @guppy.custom(FloatFloordivCompiler(), ReversingChecker(CoercingChecker()))
    def __rfloordiv__(self: float, other: float) -> float: ...

    @guppy.custom(FloatModCompiler(), ReversingChecker(CoercingChecker()))
    def __rmod__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fmul"), ReversingChecker(CoercingChecker()))
    def __rmul__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fround"))  # TODO
    def __round__(self: float) -> float: ...

    @guppy.hugr_op(
        float_op("fpow"),
        ReversingChecker(DefaultCallChecker()),
    )  # TODO
    def __rpow__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fsub"), ReversingChecker(CoercingChecker()))
    def __rsub__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fdiv"), ReversingChecker(CoercingChecker()))
    def __rtruediv__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fsub"), CoercingChecker())
    def __sub__(self: float, other: float) -> float: ...

    @guppy.hugr_op(float_op("fdiv"), CoercingChecker())
    def __truediv__(self: float, other: float) -> float: ...

    @guppy.hugr_op(
        unsupported_op("trunc_s"), CoercingChecker()
    )  # TODO `trunc_s` returns an option
    def __trunc__(self: float) -> float: ...


@guppy.extend_type(list_type_def)
class List:
    @guppy.hugr_op(unsupported_op("Append"))
    def __add__(self: list[T], other: list[T]) -> list[T]: ...

    @guppy.hugr_op(unsupported_op("IsEmpty"))
    def __bool__(self: list[T]) -> bool: ...

    @guppy.hugr_op(unsupported_op("Contains"))
    def __contains__(self: list[T], el: T) -> bool: ...

    @guppy.hugr_op(unsupported_op("AssertEmpty"))
    def __end__(self: list[T]) -> None: ...

    @guppy.hugr_op(unsupported_op("Lookup"))
    def __getitem__(self: list[T], idx: int) -> T: ...

    @guppy.hugr_op(unsupported_op("IsNotEmpty"))
    def __hasnext__(self: list[T]) -> tuple[bool, list[T]]: ...

    @guppy.custom(NoopCompiler())
    def __iter__(self: list[T]) -> list[T]: ...

    @guppy.hugr_op(unsupported_op("Length"))
    def __len__(self: list[T]) -> int: ...

    @guppy.hugr_op(unsupported_op("Repeat"))
    def __mul__(self: list[T], other: int) -> list[T]: ...

    @guppy.hugr_op(unsupported_op("Pop"))
    def __next__(self: list[T]) -> tuple[T, list[T]]: ...

    @guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
    def __new__(x): ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def __setitem__(self: list[T], idx: int, value: T) -> None: ...

    @guppy.hugr_op(unsupported_op("Append"), ReversingChecker())
    def __radd__(self: list[T], other: list[T]) -> list[T]: ...

    @guppy.hugr_op(unsupported_op("Repeat"))
    def __rmul__(self: list[T], other: int) -> list[T]: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def append(self: list[T], elt: T) -> None: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def clear(self: list[T]) -> None: ...

    @guppy.custom(NoopCompiler())  # Can be noop since lists are immutable
    def copy(self: list[T]) -> list[T]: ...

    @guppy.hugr_op(unsupported_op("Count"))
    def count(self: list[T], elt: T) -> int: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def extend(self: list[T], seq: None) -> None: ...

    @guppy.hugr_op(unsupported_op("Find"))
    def index(self: list[T], elt: T) -> int: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def pop(self: list[T], idx: int) -> None: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def remove(self: list[T], elt: T) -> None: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def reverse(self: list[T]) -> None: ...

    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
    def sort(self: list[T]) -> None: ...


linst = list


@guppy.extend_type(linst_type_def)
class Linst:
    @guppy.hugr_op(unsupported_op("Append"))
    def __add__(self: linst[L] @ owned, other: linst[L] @ owned) -> linst[L]: ...

    @guppy.hugr_op(unsupported_op("AssertEmpty"))
    def __end__(self: linst[L] @ owned) -> None: ...

    @guppy.hugr_op(unsupported_op("IsNotEmpty"))
    def __hasnext__(self: linst[L] @ owned) -> tuple[bool, linst[L]]: ...

    @guppy.custom(NoopCompiler())
    def __iter__(self: linst[L] @ owned) -> linst[L]: ...

    @guppy.hugr_op(unsupported_op("Length"))
    def __len__(self: linst[L] @ owned) -> tuple[int, linst[L]]: ...

    @guppy.hugr_op(unsupported_op("Pop"))
    def __next__(self: linst[L] @ owned) -> tuple[L, linst[L]]: ...


#    @guppy.custom(builtins, checker=UnsupportedChecker(), higher_order_value=False)
#    def __new__(x): ...
#
#    @guppy.hugr_op(builtins, unsupported_op("Append"), ReversingChecker())
#    def __radd__(self: linst[L] @owned, other: linst[L] @owned) -> linst[L]: ...
#
#    @guppy.hugr_op(unsupported_op("Repeat"))
#    def __rmul__(self: linst[L] @owned, other: int) -> linst[L]: ...
#
#    @guppy.hugr_op(unsupported_op("Push"))
#    def append(self: linst[L] @owned, elt: L @owned) -> linst[L]: ...
#
#    @guppy.hugr_op(unsupported_op("PopAt"))
#    def pop(self: linst[L] @owned, idx: int) -> tuple[L, linst[L]]: ...
#
#    @guppy.hugr_op(unsupported_op("Reverse"))
#    def reverse(self: linst[L] @owned) -> linst[L]: ...
#
#    @guppy.custom(checker=FailingChecker("Guppy lists are immutable"))
#    def sort(self: linst[T] @owned) -> None: ...


n = guppy.nat_var("n")


@guppy.extend_type(array_type_def)
class Array:
    @guppy.custom(ArrayGetitemCompiler())
    def __getitem__(self: array[L, n], idx: int) -> L: ...

    @guppy.custom(ArraySetitemCompiler())
    def __setitem__(self: array[L, n], idx: int, value: L @ owned) -> None: ...

    @guppy.custom(checker=ArrayLenChecker())
    def __len__(self: array[L, n]) -> int: ...

    @guppy.custom(NewArrayCompiler(), NewArrayChecker(), higher_order_value=False)
    def __new__(): ...


# TODO: This is a temporary hack until we have implemented the proper results mechanism.
@guppy.custom(checker=ResultChecker(), higher_order_value=False)
def result(tag, value): ...


@guppy.custom(checker=DunderChecker("__abs__"), higher_order_value=False)
def abs(x): ...


@guppy.custom(checker=CallableChecker(), higher_order_value=False)
def callable(x): ...


@guppy.custom(checker=DunderChecker("__divmod__", num_args=2), higher_order_value=False)
def divmod(x, y): ...


@guppy.custom(checker=DunderChecker("__len__"), higher_order_value=False)
def len(x): ...


@guppy.custom(checker=DunderChecker("__pow__", num_args=2), higher_order_value=False)
def pow(x, y): ...


@guppy.custom(checker=DunderChecker("__round__"), higher_order_value=False)
def round(x): ...


# Python builtins that are not supported yet:


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def aiter(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def all(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def anext(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def any(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def bin(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def breakpoint(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def bytearray(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def bytes(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def chr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def classmethod(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def compile(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def complex(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def delattr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def dict(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def dir(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def enumerate(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def eval(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def exec(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def filter(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def format(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def forozenset(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def getattr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def globals(): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def hasattr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def hash(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def help(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def hex(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def id(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def input(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def isinstance(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def issubclass(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def iter(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def locals(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def map(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def max(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def memoryview(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def min(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def next(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def object(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def oct(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def open(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def ord(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def print(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def property(x): ...


@guppy.struct
class Range:
    stop: int

    @guppy
    def __iter__(self: "Range") -> "RangeIter":
        return RangeIter(0, self.stop)  # type: ignore[call-arg]


@guppy.struct
class RangeIter:
    next: int
    stop: int

    @guppy
    def __iter__(self: "RangeIter") -> "RangeIter":
        return self

    @guppy
    def __hasnext__(self: "RangeIter") -> tuple[bool, "RangeIter"]:
        return (self.next < self.stop, self)

    @guppy
    def __next__(self: "RangeIter") -> tuple[int, "RangeIter"]:
        # Fine not to check bounds while we can only be called from inside a `for` loop.
        # if self.start >= self.stop:
        #    raise StopIteration
        return (self.next, RangeIter(self.next + 1, self.stop))  # type: ignore[call-arg]

    @guppy
    def __end__(self: "RangeIter") -> None:
        pass


@guppy
def range(stop: int) -> Range:
    """Limited version of python range().
    Only a single argument (stop/limit) is supported."""
    return Range(stop)  # type: ignore[call-arg]


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def repr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def reversed(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def set(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def setattr(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def slice(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def sorted(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def staticmethod(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def str(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def sum(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def super(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def type(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def vars(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def zip(x): ...


@guppy.custom(checker=UnsupportedChecker(), higher_order_value=False)
def __import__(x): ...
