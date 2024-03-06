from pyformlang.finite_automaton import FiniteAutomaton
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton, State
)
from scipy.sparse import kron, dok_matrix, spmatrix, csr_matrix
from math import log2, ceil

class FiniteAutomaton:
    def __init__(self, obj=None, start=set(), final=set(), mapping=dict()):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(obj, NondeterministicFiniteAutomaton):
            mat = nfa_to_matrix(obj)
            self.m, self.start, self.final, self.mapping = (
                mat.m,
                mat.start,
                mat.final,
                mat.mapping,
            )
        else:
            self.m, self.start, self.final, self.mapping = obj, start, final, mapping

    def accepts(self, word) -> bool:
        nfa = matrix_to_nfa(self)
        real_word = "".join(list(word))
        return nfa.accepts(real_word)

    def is_empty(self) -> bool:
        return len(self.m) == 0 or len(list(self.m.values())[0]) == 0

    def mapping_for(self, u) -> int:
        return self.mapping[State(u)]



def transitive_closure(mat: spmatrix) -> csr_matrix:
    closure = csr_matrix(mat)
    for _ in range(ceil(log2(mat.get_shape()[0]))):
        closure += closure @ closure
    return closure


def nfa_to_matrix(automaton: NondeterministicFiniteAutomaton) -> FiniteAutomaton:
    states = automaton.to_dict()
    len_states = len(automaton.states)
    mapping = {v: i for i, v in enumerate(automaton.states)}
    m = dict()

    for label in automaton.symbols:
        matrix = [[False] * len_states for _ in range(len_states)]
        for u, edges in states.items():
            if label in edges:
                for v in (edges[label] if isinstance(edges[label], set) else {edges[label]}):
                    matrix[mapping[u]][mapping[v]] = True
        m[label] = matrix

    return FiniteAutomaton(m, automaton.start_states, automaton.final_states, mapping)


def matrix_to_nfa(matrix, start, final, mapping):
    nfa = NondeterministicFiniteAutomaton()
    nfa.start = start.state
    nfa.final = [f.state for f in final]

    for label, mat in matrix.items():
        for i, row in enumerate(mat):
            for j, cell in enumerate(row):
                if cell:
                    nfa.add_transition(start.state, label, mapping[i].state)
                    nfa.add_transition(mapping[i].state, label, mapping[j].state)

    return nfa

def intersect_automata(
    automaton1: FiniteAutomaton, automaton2: FiniteAutomaton
) -> FiniteAutomaton:
    common_labels = automaton1.m.keys() & automaton2.m.keys()
    m = {}
    start = set()
    final = set()
    mapping = {}

    for label in common_labels:
        m[label] = kron(automaton1.m[label], automaton2.m[label])

    for state1, idx1 in automaton1.mapping.items():
        for state2, idx2 in automaton2.mapping.items():
            new_idx = len(mapping)
            combined_state = (state1, state2)
            mapping[combined_state] = new_idx
            if state1 in automaton1.start and state2 in automaton2.start:
                start.add(combined_state)
            if state1 in automaton1.final and state2 in automaton2.final:
                final.add(combined_state)

    return FiniteAutomaton(obj=m, start=start, final=final, mapping=mapping)

