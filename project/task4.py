import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order
from project.task3 import FiniteAutomaton


def reachability_with_constraints(
    fa: FiniteAutomaton, constraints_fa: FiniteAutomaton
) -> dict[int, set[int]]:
    states = len(fa.mapping)
    closure_matrix = np.random.randint(0, 2, size=(states, states)).astype(bool)
    achiev_states = {}

    for start in range(states):
        achiev = set([start])
        x, pred = breadth_first_order(
            csr_matrix(np.logical_xor(closure_matrix, closure_matrix.T)),
            i_start=start,
            return_predecessors=True
        )
        achiev.update({p for p, q in enumerate(pred) if p != start and q != -9999})
        achiev_states[start] = achiev

    return achiev_states
