from pyformlang.finite_automaton import FiniteAutomaton
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton, State
)
from scipy.sparse import kron, dok_matrix, spmatrix, csr_matrix
from math import log2, ceil


class FiniteAutomaton:
    def __init__(self, obj=None, start=None, final=None, mapping=None):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(obj, NondeterministicFiniteAutomaton):
            self.matrix, self.start, self.final, self.mapping = nfa_to_matrix(obj)
        else:
            self.matrix = obj if obj is not None else []
            self.start = start if start is not None else set()
            self.final = final if final is not None else set()
            self.mapping = mapping if mapping is not None else {}

    def accepts(self, word):
        nfa = matrix_to_nfa(self)
        return nfa.accepts(word)

    def is_empty(self):
        if len(self.matrix) == 0:
            return True
        for state in self.matrix:
            if state:
                return False
        return True

    def mapping_for(self, u):
        return self.mapping[State(u)]



def transitive_closure(mat: spmatrix) -> csr_matrix:
    closure = csr_matrix(mat)
    for _ in range(ceil(log2(mat.get_shape()[0]))):
        closure += closure @ closure
    return closure


def nfa_to_matrix(automaton):
    states = automaton.to_dict()
    len_states = len(automaton.states)
    mapping = {v: i for i, v in enumerate(automaton.states)}
    m = dict()

    for label in automaton.symbols:
        matrix = [[False] * len_states for _ in range(len_states)]
        for u, transitions in states.items():
            for v in transitions.get(label, []):
                matrix[mapping[u]][mapping[v]] = True
        m[label] = matrix

    return m, State(automaton.start), set(map(State, automaton.final)), mapping

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

def intersect_automata(automaton1, automaton2):
    common_labels = automaton1.matrix.keys() & automaton2.matrix.keys()
    m = {}
    start = set()
    final = set()
    mapping = {}

    for label in common_labels:
        m[label] = kron(automaton1.matrix[label], automaton2.matrix[label])

    for state1, idx1 in automaton1.mapping.items():
        for state2, idx2 in automaton2.mapping.items():
            new_idx = len(mapping)
            mapping[(state1.state, state2.state)] = new_idx
            if state1 == automaton1.start and state2 == automaton2.start:
                start.add(new_idx)
            if state1 in automaton1.final and state2 in automaton2.final:
                final.add(new_idx)

    return FiniteAutomaton(obj=m, start=start, final=final, mapping=mapping)
