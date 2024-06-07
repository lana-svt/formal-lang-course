from scipy.sparse import dok_matrix, block_diag

from project.task3 import FiniteAutomaton


def reachability_with_constraints(
    automaton: FiniteAutomaton, constraint_automaton: FiniteAutomaton
) -> dict[int, set[int]]:
    m, n = constraint_automaton.size(), automaton.size()

    def get_front(start_state_index):
        front = dok_matrix((m, m + n), dtype=bool)
        for i in constraint_automaton.start_indices():
            front[i, i] = True
        for i in range(m):
            front[i, start_state_index + m] = True
        return front

    def diag(mat):
        result = dok_matrix(mat.shape, dtype=bool)
        for i in range(mat.shape[0]):
            for j in range(mat.shape[0]):
                if mat[j, i]:
                    result[i] += mat[j]
        return result

    common_labels = automaton.labels() & constraint_automaton.labels()
    result = {s: set() for s in automaton.start_states}
    adj = {
        label: block_diag(
            (constraint_automaton.transitions[label], automaton.transitions[label])
        )
        for label in common_labels
    }

    for v in automaton.start_indices():
        front = get_front(v)
        last_hash = -1
        for _ in range(m * n):
            front = sum(
                [dok_matrix((m, m + n), dtype=bool)]
                + [diag(front @ adj[label]) for label in common_labels]
            )
            fr = front[:, m:].nonzero()
            for a, b in zip(fr[0], fr[1]):
                if (
                    a in constraint_automaton.final_indices()
                        and b in automaton.final_indices()
                ):
                    result[v].add(b)
                if hash(str(fr)) == last_hash:
                    break
                last_hash = hash(str(fr))

    return result
