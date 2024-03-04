from typing import List, Tuple, Set, Iterable, Dict, Any
import networkx as nx
from networkx.classes.reportviews import NodeView
import numpy as np
from pyformlang.finite_automaton import FiniteAutomaton, State, Symbol
from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
)
from scipy.sparse import kron, dok_matrix, coo_matrix, spmatrix, csr_matrix
from task2 import regex_to_dfa, graph_to_nfa
from math import log2, ceil


class FiniteAutomaton:
    def __init__(self, transitions: dict, start_states: set, final_states: set):
        self.transitions = transitions
        self.start_states = start_states
        self.final_states = final_states


    def to_sparse_matrix(self):
        states = list(self.transitions.keys())
        n_states = len(states)
        symbols = set()
        for state in self.transitions.values():
            symbols.update(state.keys())
        n_symbols = len(symbols)

        matrix = dok_matrix((n_states, n_symbols), dtype=bool)
        symbol_mapping = {symbol: idx for idx, symbol in enumerate(symbols)}

        for row_idx, state in enumerate(states):
            for symbol, next_state in self.transitions[state].items():
                col_idx = symbol_mapping[symbol]
                matrix[row_idx, col_idx] = True

        return matrix

    def accepts(self, word: Iterable[Symbol]) -> bool:
        current_states = set(self.start_states)
        for symbol in word:
            next_states = set()
            for state in current_states:
                transitions = self.transitions.get(state, {}).get(symbol, set())
                next_states.update(transitions)
            current_states = next_states
        return bool(current_states.intersection(self.final_states))

    def is_empty(self) -> bool:
        transitive_closure = self._transitive_closure()

        for start_state in self.start_states:
            for final_state in self.final_states:
                if transitive_closure[start_state, final_state]:
                    return False
        return True

    def transitive_closure(mat: spmatrix) -> csr_matrix:
        closure = csr_matrix(mat)

        for _ in range(ceil(log2(mat.get_shape()[0]))):
            closure += closure @ closure

        return closure

def from_dfa(cls, dfa: DeterministicFiniteAutomaton):
    transitions = {}
    for state in dfa.states:
        transitions[state] = {}
        for symbol in dfa.symbols:
            next_state = dfa.transitions.get(state, {}).get(symbol)
            if next_state is not None:
                transitions[state][symbol] = next_state
    return cls(transitions, dfa.start_state, dfa.final_states)

def from_nfa(cls, nfa: NondeterministicFiniteAutomaton):
    transitions = {}
    for state in nfa.states:
        transitions[state] = {}
        for symbol in nfa.symbols:
            next_states = nfa.transitions.get(state, {}).get(symbol, set())
            for next_state in next_states:
                transitions[state].setdefault(symbol, set()).add(next_state)
    return cls(transitions, nfa.start_states, nfa.final_states)