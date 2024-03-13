from pyformlang.finite_automaton import (
    DeterministicFiniteAutomaton,
    NondeterministicFiniteAutomaton,
    State,
)
from scipy.sparse import dok_matrix, kron
from itertools import product
from project.task2 import graph_to_nfa, regex_to_dfa
from networkx import MultiDiGraph
from typing import List, Tuple, Set


class FiniteAutomaton:
    def __init__(self, obj=None, start=None, final=None, mapping=None):
        if isinstance(obj, DeterministicFiniteAutomaton) or isinstance(
            obj, NondeterministicFiniteAutomaton
        ):
            mat = nfa_to_matrix(obj)
            self.m, self.start, self.final, self.mapping = (
                mat.m,
                mat.start,
                mat.final,
                mat.mapping,
            )
        else:
            self.m = obj if obj is not None else []
            self.start = start if start is not None else set()
            self.final = final if final is not None else set()
            self.mapping = mapping if mapping is not None else {}

    def accepts(self, word) -> bool:
        nfa = matrix_to_nfa(self)
        return nfa.accepts("".join(list(word)))

    def is_empty(self) -> bool:
        return not any(self.m.values()) if self.m else True

    def mapping_for(self, u) -> int:
        state_u = State(u)
        return self.mapping.get(state_u, 0)


def nfa_to_matrix(automaton: NondeterministicFiniteAutomaton) -> FiniteAutomaton:
    states = automaton.to_dict()
    len_states = len(automaton.states)
    mapping = {v: i for i, v in enumerate(automaton.states)}
    m = {
        label: dok_matrix((len_states, len_states), dtype=bool)
        for label in automaton.symbols
    }

    for u, edges in states.items():
        for label, v_set in {
            k: [v] if not isinstance(v, set) else list(v) for k, v in edges.items()
        }.items():
            for v in v_set:
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
    automaton1: FiniteAutomaton, automaton2: FiniteAutomaton
) -> FiniteAutomaton:
    m = {
        label: kron(automaton1.m[label], automaton2.m[label], "csr")
        for label in automaton1.m.keys() & automaton2.m.keys()
    }
    start = {
        State(len(automaton2.mapping) * automaton1.mapping[u] + automaton2.mapping[v])
        for u, v in product(automaton1.start, automaton2.start)
    }
    final = {
        State(len(automaton2.mapping) * automaton1.mapping[u] + automaton2.mapping[v])
        for u, v in product(automaton1.final, automaton2.final)
    }
    mapping = {
        len(automaton2.mapping) * i + j: len(automaton2.mapping) * i + j
        for i in automaton1.mapping.values()
        for j in automaton2.mapping.values()
    }

    return FiniteAutomaton(m, start, final, mapping)


def paths_ends(
    graph: MultiDiGraph, start_nodes: Set[int], final_nodes: Set[int], regex: str
) -> List[Tuple[object, object]]:
    dfa = nfa_to_matrix(regex_to_dfa(regex))
    nfa = nfa_to_matrix(graph_to_nfa(graph, start_nodes, final_nodes))
    intersection = intersect_automata(nfa, dfa)
    closure = transitive_closure(intersection)

    mapping = {}
    reg_size = len(dfa.mapping)

    for i, v in nfa.mapping.items():
        mapping[v] = i

    result = [
        (mapping[u // reg_size], mapping[v // reg_size])
        for u, v in zip(*closure.nonzero())
        if u in intersection.start and v in intersection.final
    ]

    return result
