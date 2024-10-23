from typing import Literal
from quark.circuit import QuantumCircuit, generate_ghz_state, Transpile

def call_quarkcircuit_transpile(
        qc: QuantumCircuit | str | list,
        chip_name: Literal['Baihua'] = 'Baihua',
        use_priority: bool = True,
        initial_mapping: list | None = None,
        coupling_map: list[tuple] | None = None,
        optimize_level = 0,
        ):
    
    # qc， compile, backend, level, 
    qct = Transpile(qc,
                    chip_name=chip_name,
                    use_priority=use_priority,
                    initial_mapping=initial_mapping,
                    coupling_map=coupling_map).run(optimize_level=optimize_level)

    return qct.to_qlisp


if __name__ == '__main__':
    nqubits = 4
    qc = generate_ghz_state(nqubits)
    qct_qlisp = call_quarkcircuit_transpile(qc)
    print(qct_qlisp)