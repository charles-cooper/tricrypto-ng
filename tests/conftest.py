pytest_plugins = [
    "tests.boa.fixtures.accounts",
    "tests.boa.fixtures.tokens",
    "tests.boa.fixtures.functions",
    "tests.boa.fixtures.pool",
    "tests.boa.fixtures.factory",
]

import boa
boa.vyper.compiler_utils.set_vyper_evm_version("cancun")

# patch tload / tstore to use sload/sstore for now
boa.patch_opcode(0x5C, boa.env.vm.state.computation_class.opcodes[0x54])
boa.patch_opcode(0x5D, boa.env.vm.state.computation_class.opcodes[0x55])
