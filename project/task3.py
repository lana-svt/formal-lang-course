from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
    State,
)
from scipy.sparse import dok_matrix, kron
from networkx import MultiDiGraph
from project.task2 import graph_to_nfa, regex_to_dfa


class FiniteAutomaton:

    transitions = None
    start_states = None
    final_states = None
    states_mapping = None
    is_deterministic = True
    epsilon_symbol = None
    number_of_states = None

    def __init__(
        self,
        obj: any,
        start_states=set(),
        final_states=set(),
        states_mapping=dict(),
        matrix_class=dok_matrix,
    ):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(
            obj, NondeterministicFiniteAutomaton
        ):
            mat = nfa_to_mat(obj, matrix_class=matrix_class)
            (
                self.transitions,
                self.start_states,
                self.final_states,
                self.states_mapping,
            ) = (mat.transitions,
                 mat.start_states,
                 mat.final_states,
                 mat.states_mapping
                 )
        else:
            self.transitions = obj
            self.final_states = final_states
            self.start_states = start_states
            self.states_mapping = states_mapping

    def accepts(self, word) -> bool:
        nfa = mat_to_nfa(self)
        return nfa.accepts("".join(list(word)))

    def is_empty(self) -> bool:
        closure = transitive_closure(self)
        for ss in self.start_states:
            for tt in self.final_states:
                ss_index = self.states_mapping[ss]
                tt_index = self.states_mapping[tt]
                try:
                    if closure[ss_index, tt_index]:
                        return False
                except:
                    pass
        return True

    def final_indices(self):
        return [self.map_state_index(t) for t in self.final_states]

    def start_indices(self):
        return [self.map_state_index(t) for t in self.start_states]

    def labels(self):
        return (
            self.states_mapping.keys()
            if self.is_deterministic
            else self.transitions.keys()
        )

    def size(self):
        return len(self.states_mapping)

    def map_state_index(self, state):
        return self.states_mapping[State(state)]

    def indices_dict(self):
        return {i: v for v, i in self.states_mapping.items()}


def nfa_to_mat(
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


def mat_to_nfa(automaton: FiniteAutomaton) -> NondeterministicFiniteAutomaton:
    nfa = NondeterministicFiniteAutomaton()

    for label in automaton.transitions.keys():
        n = automaton.transitions[label].shape[0]
        for u in range(n):
            for v in range(n):
                if automaton.transitions[label][u, v]:
                    nfa.add_transition(
                        automaton.map_state_index(u),
                        label,
                        automaton.map_state_index(v),
                    )

    for start_state in automaton.start_states:
        nfa.add_start_state(automaton.map_state_index(start_state))
    for final_state in automaton.final_states:
        nfa.add_final_state(automaton.map_state_index(final_state))

    return nfa


def transitive_closure(automaton: FiniteAutomaton):
    if len(automaton.transitions.values()) == 0:
        return dok_matrix((0, 0), dtype=bool)
    adj = sum(automaton.transitions.values())
    last_ = -1
    while adj.count_nonzero() != last_:
        last_ = adj.count_nonzero()
        adj += adj @ adj

    return adj


def intersect_automata(
    automaton1: FiniteAutomaton,
    automaton2: FiniteAutomaton,
    matrix_class_id="csr",
    is_graph=True,
) -> FiniteAutomaton:
    automaton1.is_deterministic = not is_graph
    automaton2.is_deterministic = not is_graph
    labels = automaton1.labels() & automaton2.labels()
    transitions = dict()
    start_states = set()
    final_states = set()
    states_mapping = dict()

    for label in labels:
        transitions[label] = kron(
            automaton1.transitions[label],
            automaton2.transitions[label],
            matrix_class_id
        )

    for u, i in automaton1.states_mapping.items():
        for v, j in automaton2.states_mapping.items():
            k = len(automaton2.states_mapping) * i + j
            states_mapping[State(k)] = k

            if u in automaton1.start_states and v in automaton2.start_states:
                start_states.add(State(k))

            if u in automaton1.final_states and v in automaton2.final_states:
                final_states.add(State(k))

    return FiniteAutomaton(transitions, start_states, final_states, states_mapping)


def paths_ends(
    graph: MultiDiGraph,
    start_nodes: set[int],
    final_nodes: set[int],
    regex: str,
    matrix_class=dok_matrix,
    matrix_class_id="csr",
) -> list[tuple[object, object]]:
    graph_nfa = nfa_to_mat(
        graph_to_nfa(graph, start_nodes, final_nodes), matrix_class=matrix_class
    )
    regex_dfa = nfa_to_mat(regex_to_dfa(regex), matrix_class=matrix_class)

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
