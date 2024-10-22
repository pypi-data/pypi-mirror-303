from guppylang.decorator import guppy
from guppylang.module import GuppyModule
from guppylang.prelude.builtins import owned
from guppylang.prelude.quantum import qubit
from guppylang.prelude.quantum_functional import h

module = GuppyModule("test")
module.load(qubit, h)


@guppy(module)
def foo(q: qubit @owned) -> None:
    h(q)


module.compile()
