from pyformlang.finite_automaton import FiniteAutomaton
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
)
from scipy.sparse import kron, dok_matrix, spmatrix, csr_matrix
from math import log2, ceil


class FiniteAutomaton:
    def __init__(self, obj=None, start=None, final=None, mapping=None):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(obj, NondeterministicFiniteAutomaton):
            self.m, self.start, self.final, self.mapping = nfa_to_matrix(obj)
        else:
            self.m = obj if obj is not None else []
            self.start = start if start is not None else set()
            self.final = final if final is not None else set()
            self.mapping = mapping if mapping is not None else {}

    def accepts(self, word):
        nfa = matrix_to_nfa(self)
        return nfa.accepts(word)

    def is_empty(self):
        if len(self.m) == 0:
            return True
        for state in self.m:
            if state:
                return False
        return True

    def mapping_for(self, u):
        return self.mapping.get(u, {})


def transitive_closure(mat: spmatrix) -> csr_matrix:
    closure = csr_matrix(mat)
    for _ in range(ceil(log2(mat.get_shape()[0]))):
        closure += closure @ closure
    return closure


def nfa_to_matrix(automaton):
    #states = {}
    len_states = len(automaton.states)
    mapping = {state: index for index, state in enumerate(automaton.states)}
    m = {}

    for symbol in automaton.symbols:
        m[symbol] = dok_matrix((len_states, len_states), dtype=bool)

    for u, edges in automaton.states.items():
        for label, targets in edges.items():
            for v in targets:
                m[label][mapping[u], mapping[v]] = True

    fa = FiniteAutomaton(m, {mapping[state] for state in automaton.start_states},
                         {mapping[state] for state in automaton.accept_states}, mapping)

    return fa

def matrix_to_nfa(automaton):
    nfa = NondeterministicFiniteAutomaton()

    for label in automaton.m.keys():
        m_size = automaton.m[label].shape[0]

        for u in range(m_size):
            for v in range(m_size):
                if automaton.m[label][u, v]:
                    nfa.add_transition(u, label, v)

    for start_state in automaton.start:
        nfa.add_start_state(start_state)

    for final_state in automaton.final:
        nfa.add_final_state(final_state)

    return nfa

def intersect_automata(automaton1, automaton2):
    labels = set(automaton1.m.keys()) & set(automaton2.m.keys())

    m = {}
    start = set()
    final = set()
    mapping = {}

    for label in labels:
        m[label] = kron(automaton1.m[label], automaton2.m[label])

    for u, u_index in automaton1.mapping.items():
        for v, v_index in automaton2.mapping.items():
            k = len(mapping)
            mapping[(u_index, v_index)] = k

            if u in automaton1.start and v in automaton2.start:
                start.add(k)
            if u in automaton1.final and v in automaton2.final:
                final.add(k)

    return FiniteAutomaton(m, start, final, mapping)
