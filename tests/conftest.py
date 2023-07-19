pytest_plugins = [
    "tests.boa.fixtures.accounts",
    "tests.boa.fixtures.tokens",
    "tests.boa.fixtures.functions",
    "tests.boa.fixtures.pool",
    "tests.boa.fixtures.factory",
]

from vyper.compiler.settings import OptimizationLevel
import vyper.codegen.core

vyper.codegen.core._opt_level = OptimizationLevel.CODESIZE
