from project.task8 import cfg_to_rsm
from pyformlang.cfg import CFG
from pyformlang.finite_automaton import State
from pyformlang.rsa import RecursiveAutomaton
import networkx as nx
from copy import deepcopy
from project.task8 import cfg_to_rsm
from pyformlang.cfg import CFG
from pyformlang.finite_automaton import State
from pyformlang.rsa import RecursiveAutomaton
import networkx as nx
from collections import deque


def cfpq_with_gll(
    automaton: RecursiveAutomaton,
    digraph: nx.DiGraph,
    init_nodes: set[int] = None,
    end_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    if isinstance(automaton, CFG):
        automaton = cfg_to_rsm(automaton)

    if init_nodes is None:
        init_nodes = set(digraph.nodes)

    if end_nodes is None:
        end_nodes = set(digraph.nodes)

    nonterm_start_rsm = automaton.initial_label.value if automaton.initial_label.value is not None else "S"
    start_rsm = automaton.boxes[automaton.initial_label].dfa.start_state.value

    res = set()
    visited = set()
    queue = deque()

    for sn in init_nodes:
        queue.append((nonterm_start_rsm, sn, sn))

    start_dfa = automaton.boxes[nonterm_start_rsm].dfa.to_dict()
    start_dfa.setdefault(State(start_rsm), dict())

    while queue:
        current_nonterm, current_node, path_start = queue.popleft()

        if (current_node, (path_start, current_nonterm)) in visited:
            continue
        visited.add((current_node, (path_start, current_nonterm)))

        if current_node in end_nodes and current_nonterm == start_rsm:
            res.add((path_start, current_node))

        for symbol, _ in start_dfa.items():
            if symbol in automaton.labels:
                new_state = (current_nonterm, current_node, symbol.value)
                if new_state not in visited:
                    queue.append((symbol.value, current_node, path_start))

        for neighbor in digraph.neighbors(current_node):
            if (current_nonterm, neighbor, path_start) not in visited:
                queue.append((current_nonterm, neighbor, path_start))

    return res
