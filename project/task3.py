from typing import Iterable
from networkx import MultiDiGraph
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
    State,
)
import numpy as np
from scipy.sparse import dok_matrix, kron, spmatrix, csr_matrix
from math import log2, ceil




class FiniteAutomaton:
    def __init__(self, obj=None, start=None, final=None, mapping=None):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(obj, NondeterministicFiniteAutomaton):
            self.m, self.start, self.final, self.mapping = nfa_to_mat(obj)
        else:
            self.m = obj if obj is not None else []
            self.start = start if start is not None else set()
            self.final = final if final is not None else set()
            self.mapping = mapping if mapping is not None else {}

    def accepts(self, word):
        nfa = mat_to_nfa(self)
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

def as_set(obj):
    if not isinstance(obj, set):
        return {obj}
    return obj

def nfa_to_mat(automaton: NondeterministicFiniteAutomaton) -> FiniteAutomaton:
    states = automaton.to_dict()
    len_states = len(automaton.states)
    mapping = {v: i for i, v in enumerate(automaton.states)}
    m = dict()

    for label in automaton.symbols:
        m[label] = dok_matrix((len_states, len_states), dtype=bool)
        for u, edges in states.items():
            if label in edges:
                for v in as_set(edges[label]):
                    m[label][mapping[u], mapping[v]] = True

    return FiniteAutomaton(m, automaton.start_states, automaton.final_states, mapping)


def mat_to_nfa(automaton: FiniteAutomaton) -> NondeterministicFiniteAutomaton:
    nfa = NondeterministicFiniteAutomaton()

    for label in automaton.m.keys():
        m_size = automaton.m[label].shape[0]
        for u in range(m_size):
            for v in range(m_size):
                if automaton.m[label][u, v]:
                    nfa.add_transition(
                        automaton.mapping_for(u), label, automaton.mapping_for(v)
                    )

    for s in automaton.start:
        nfa.add_start_state(automaton.mapping_for(s))
    for s in automaton.final:
        nfa.add_final_state(automaton.mapping_for(s))

    return nfa




def transitive_closure(mat: spmatrix) -> csr_matrix:
    closure = csr_matrix(mat)
    for _ in range(ceil(log2(mat.get_shape()[0]))):
        closure += closure @ closure
    return closure


def intersect_automata(automaton1: FiniteAutomaton,
                       automaton2: FiniteAutomaton) -> FiniteAutomaton:
    result = FiniteAutomaton()

    matrices1 = automaton1.m
    matrices2 = automaton2.m

    symbols = set(matrices1.keys()).intersection(matrices2.keys())

    result_matrices = {}
    for s in symbols:
        matrix1 = matrices1[s]
        matrix2 = matrices2[s]
        intersection_matrix = np.logical_and(matrix1, matrix2)
        result_matrices[s] = intersection_matrix

    result.m = result_matrices

    result.start = automaton1.start.intersection(automaton2.start)
    result.final = automaton1.final.intersection(automaton2.final)

    return result


# from pyformlang.finite_automaton import FiniteAutomaton as PyFormlangFA
# from pyformlang.finite_automaton import (
#     DeterministicFiniteAutomaton,
#     NondeterministicFiniteAutomaton, State
# )
# from scipy.sparse import kron, csr_matrix
# from math import log2, ceil
# import numpy as np
#
# class FiniteAutomaton:
#     def __init__(self, obj=None, start=set(), final=set(), mapping=dict()):
#         if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(obj, NondeterministicFiniteAutomaton):
#             mat = nfa_to_matrix(obj)
#             self.m, self.start, self.final, self.mapping = (
#                 mat.m,
#                 mat.start,
#                 mat.final,
#                 mat.mapping,
#             )
#         else:
#             self.m, self.start, self.final, self.mapping = obj, start, final, mapping
#
#     def accepts(self, word) -> bool:
#         nfa = matrix_to_nfa(self, self.start, self.final, self.mapping)
#         real_word = "".join(list(word))
#         return nfa.accepts(real_word)
#
#     def is_empty(self) -> bool:
#         return len(self.m) == 0 or len(list(self.m.values())[0]) == 0
#
#     def mapping_for(self, u) -> int:
#         return self.mapping[State(u)]
#
# def transitive_closure(mat: csr_matrix) -> csr_matrix:
#     closure = csr_matrix(mat)
#     for _ in range(ceil(log2(mat.get_shape()[0]))):
#         closure += closure.dot(closure)
#     return closure
#
# def nfa_to_matrix(automaton: NondeterministicFiniteAutomaton) -> FiniteAutomaton:
#     states = automaton.to_dict()
#     len_states = len(automaton.states)
#     mapping = {v: i for i, v in enumerate(automaton.states)}
#     m = dict()
#
#     for label in automaton.symbols:
#         matrix = [[False] * len_states for _ in range(len_states)]
#         for u, edges in states.items():
#             if label in edges:
#                 for v in (edges[label] if isinstance(edges[label], set) else {edges[label]}):
#                     matrix[mapping[u]][mapping[v]] = True
#         m[label] = matrix
#
#     return FiniteAutomaton(m, automaton.start_states, automaton.final_states, mapping)
#
# def matrix_to_nfa(matrix, start, final, mapping):
#     nfa = NondeterministicFiniteAutomaton()
#     nfa.start = list(start)[0]
#     nfa.final = [f.state for f in final]
#
#     for label, mat in matrix.items():
#         for i, row in enumerate(mat):
#             for j, cell in enumerate(row):
#                 if cell:
#                     nfa.add_transition(list(start)[0], label, mapping[i].state)
#                     nfa.add_transition(mapping[i].state, label, mapping[j].state)
#
#     return nfa
#
# def intersect_automata(automaton1: FiniteAutomaton,
#                        automaton2: FiniteAutomaton) -> FiniteAutomaton:
#     result = FiniteAutomaton()
#
#     matrices1 = automaton1.m
#     matrices2 = automaton2.m
#
#     symbols = set(matrices1.keys()).intersection(matrices2.keys())
#
#     result_matrices = {}
#     for s in symbols:
#         matrix1 = matrices1[s]
#         matrix2 = matrices2[s]
#         intersection_matrix = np.logical_and(matrix1, matrix2)
#         result_matrices[s] = intersection_matrix
#
#     # Устанавливаем матрицы переходов для результирующего автомата
#     result.m = result_matrices
#
#     # Устанавливаем начальные и конечные состояния для результирующего автомата
#     result.start = automaton1.start.intersection(automaton2.start)
#     result.final = automaton1.final.intersection(automaton2.final)
#
#     return result
