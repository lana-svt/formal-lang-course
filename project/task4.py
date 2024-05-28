from scipy.sparse import dok_matrix, block_diag
from project.task3 import FiniteAutomaton

def reachability_with_constraints(
    fa: FiniteAutomaton, constraints_fa: FiniteAutomaton
) -> dict[int, set[int]]:
    m, n = constraints_fa.size(), fa.size()
    result = {s: set() for s in fa.start_states}

    common_labels = fa.labels() & constraints_fa.labels()
    adj = {
        label: block_diag((constraints_fa.transitions[label], fa.transitions[label]))
        for label in common_labels
    }

    for v in fa.start_states:
        front = dok_matrix((m, m + n), dtype=bool)
        for i in constraints_fa.start_indices():
            front[i, i] = True
        for i in range(m):
            front[i, v + m] = True

        last_front_hash = -1
        for _ in range(m * n):
            front = sum(
                [dok_matrix((m, m + n), dtype=bool)]
                + [front @ adj[label] for label in common_labels]
            )

            front_indices = front[:, m:].nonzero()
            for a, b in zip(front_indices[0], front_indices[1]):
                if a in constraints_fa.final_indices() and b in fa.final_indices():
                    result[v].add(b)
            current_front_hash = hash(str(front_indices))
            if current_front_hash == last_front_hash:
                break
            last_front_hash = current_front_hash

    return result

