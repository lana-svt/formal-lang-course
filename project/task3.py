from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
    State,
)
from scipy.sparse import dok_matrix, kron
from task2 import graph_to_nfa, regex_to_dfa
from networkx import MultiDiGraph


class FiniteAutomaton:

    def __init__(
        self,
        obj: any,
        start_set=set(),
        final_set=set(),
        mapping_dict=dict(),
        matrix_class=dok_matrix,
    ):
        self.m, self.start, self.final, self.mapping, self.g = (
            None,
            None,
            None,
            None,
            True
        )

        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(
            obj, NondeterministicFiniteAutomaton
        ):
            mat = nfa_to_matrix(obj, matrix_class=matrix_class)
            self.m, self.start, self.final, self.mapping = (
                mat.m,
                mat.start,
                mat.final,
                mat.mapping,
            )
        else:
            self.m, self.start, self.final, self.mapping = (
                obj,
                start_set,
                final_set,
                mapping_dict
            )

    def accepts(self, word) -> bool:
        nfa = matrix_to_nfa(self)
        return nfa.accepts("".join(list(word)))

    def is_empty(self) -> bool:
        return not any(self.m.values()) if self.m else True

    def mapping_for(self, u) -> int:
        state_u = State(u)
        return self.mapping.get(state_u, 0)

    def size(self):
        return len(self.mapping)

    def start_inds(self):
        return [self.mapping_for(t) for t in self.start]

    def final_inds(self):
        return [self.mapping_for(t) for t in self.final]

    def indexes_dict(self):
        return {i: v for v, i in self.mapping.items()}

    def labels(self):
        return self.mapping.keys() if self.g else self.m.keys()


def nfa_to_matrix(
    automaton: NondeterministicFiniteAutomaton, matrix_class=dok_matrix
) -> FiniteAutomaton:
    states = automaton.to_dict()
    len_states = len(automaton.states)
    mapping = {v: i for i, v in enumerate(automaton.states)}
    m = dict()

    for label in automaton.symbols:
        m[label] = matrix_class((len_states, len_states), dtype=bool)
        for u, edges in states.items():
            if label in edges:
                targets = edges[label]
                if not isinstance(targets, set):
                    targets = {targets}
                for v in targets:
                    m[label][mapping[u], mapping[v]] = True

    return FiniteAutomaton(m, automaton.start_states, automaton.final_states, mapping)


def matrix_to_nfa(automaton: FiniteAutomaton) -> NondeterministicFiniteAutomaton:
    nfa = NondeterministicFiniteAutomaton()
    mapping_reverse = {v: k for k, v in automaton.mapping.items()}

    for label in automaton.m.keys():
        m_size = automaton.m[label].shape[0]
        for u in range(m_size):
            for v in range(m_size):
                if automaton.m[label][u, v]:
                    nfa.add_transition(mapping_reverse[u], label, mapping_reverse[v])

    for s in automaton.start:
        nfa.add_start_state(mapping_reverse[s])
    for s in automaton.final:
        nfa.add_final_state(mapping_reverse[s])

    return nfa


def transitive_closure(automaton: FiniteAutomaton):
    if len(automaton.m.values()) == 0:
        return dok_matrix((0, 0), dtype=bool)
    closure = sum(automaton.m.values())
    for _ in range(closure.shape[0]):
        closure += closure @ closure
    return closure


def intersect_automata(
    automaton1: FiniteAutomaton,
    automaton2: FiniteAutomaton,
    matrix_class_id="csr",
    g=True,
) -> FiniteAutomaton:
    automaton1.g = automaton2.g = not g
    labels = automaton1.labels() & automaton2.labels()
    m = {
        label: kron(automaton1.m[label], automaton2.m[label], matrix_class_id)
        for label in labels
    }
    mapping = {
        State(len(automaton2.mapping) * i + j): len(automaton2.mapping) * i + j
        for u, i in automaton1.mapping.items()
        for v, j in automaton2.mapping.items()
    }

    start = {
        State(k)
        for k in mapping.values()
        if any(
            u in automaton1.start and v in automaton2.start
            for u, i in automaton1.mapping.items()
            for v, j in automaton2.mapping.items()
            if len(automaton2.mapping) * i + j == k
        )
    }

    final = {
        State(k)
        for k in mapping.values()
        if any(
            u in automaton1.final and v in automaton2.final
            for u, i in automaton1.mapping.items()
            for v, j in automaton2.mapping.items()
            if len(automaton2.mapping) * i + j == k
        )
    }

    return FiniteAutomaton(m, start, final, mapping)


def paths_ends(
    graph: MultiDiGraph,
    start_nodes: set[int],
    final_nodes: set[int],
    regex: str,
    matrix_class=dok_matrix,
    matrix_class_id="csr",
) -> list[tuple[object, object]]:
    graph_nfa = nfa_to_matrix(
        graph_to_nfa(graph, start_nodes, final_nodes), matrix_class=matrix_class
    )
    regex_dfa = nfa_to_matrix(regex_to_dfa(regex), matrix_class=matrix_class)

    intersection = intersect_automata(
        graph_nfa, regex_dfa, matrix_class_id=matrix_class_id, g=False
    )
    closure = transitive_closure(intersection)
    mapping = {v: i for i, v in graph_nfa.mapping.items()}
    result = []
    for u, v in zip(*closure.nonzero()):
        if u in intersection.start and v in intersection.final:
            result.append(
                (mapping[u // regex_dfa.size()], mapping[v // regex_dfa.size()])
            )

    return result
