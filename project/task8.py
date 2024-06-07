import pyformlang
import scipy
from networkx import DiGraph
from project import task3
from pyformlang.cfg import Epsilon
from pyformlang.finite_automaton import State, Symbol
from pyformlang.regular_expression import Regex
from pyformlang.rsa import Box
from scipy.sparse import dok_matrix
from pyformlang.cfg import CFG
from pyformlang.rsa import RecursiveAutomaton
from project.task2 import graph_to_nfa


def cfg_to_rsm(cfg: CFG) -> RecursiveAutomaton:
    productions_dict = {}

    for production_item in cfg.productions:
        body_regex = (
            Epsilon().to_text()
            if len(production_item.body) == 0
            else " ".join(var.value for var in production_item.body)
        )
        head_symbol = Symbol(production_item.head)
        if head_symbol not in productions_dict:
            productions_dict[head_symbol] = [body_regex]
        else:
            productions_dict[head_symbol].append(body_regex)

    result_dict = {}

    for symbol, regex_list in productions_dict.items():
        combined_regex = "|".join(regex_list)
        regex = Regex(combined_regex)
        result_dict[Symbol(symbol)] = Box(
            regex.to_epsilon_nfa().to_deterministic(), Symbol(symbol)
        )

    return RecursiveAutomaton(
        set(result_dict.keys()), Symbol("S"), set(result_dict.values())
    )


def ebnf_to_rsm(ebnf: str) -> RecursiveAutomaton:
    productions_dict = {}

    for production_line in ebnf.splitlines():
        production_line = production_line.strip()
        if "->" not in production_line:
            continue

        head, body = production_line.split("->")
        head = head.strip()
        body = body.strip() if body.strip() != "" else Epsilon().to_text()

        if head not in productions_dict:
            productions_dict[head] = [body]
        else:
            productions_dict[head].append(body)

    result_dict = {}

    for symbol, regex_list in productions_dict.items():
        combined_regex = "|".join(regex_list)
        regex = Regex(combined_regex)
        result_dict[Symbol(symbol)] = Box(
            regex.to_epsilon_nfa().to_deterministic(), Symbol(symbol)
        )

    return RecursiveAutomaton(
        set(result_dict.keys()), Symbol("S"), set(result_dict.values())
    )


def cfpq_with_tensor(
    rsm: pyformlang.rsa.RecursiveAutomaton,
    graph: DiGraph,
    start_nodes: set[int] = None,
    final_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    if isinstance(rsm, CFG):
        rsm = cfg_to_rsm(rsm)

    states = set()
    start_states = set()
    final_states = set()
    null_symb = set()

    for v, a in rsm.boxes.items():
        for state in a.dfa.states:
            s = State((v, state.value))
            states.add(s)
            if state in a.dfa.start_states:
                start_states.add(s)
            if state in a.dfa.final_states:
                final_states.add(s)

    ls = len(states)
    states_map = {}
    for i, v in enumerate(sorted(states, key=lambda x: x.value[1])):
        states_map[v] = i

    m = dict()
    for var, p in rsm.boxes.items():
        for src, transition in p.dfa.to_dict().items():
            for symbol, dst in transition.items():
                label = symbol.value
                if label not in m:
                    m[label] = dok_matrix((ls, ls), dtype=bool)

                dst = {dst} if not isinstance(dst, set) else dst
                for target in dst:
                    sts_src = states_map[State((var, src.value))]
                    sts_target = states_map[State((var, target.value))]
                    m[label][sts_src, sts_target] = True
                if isinstance(dst, Epsilon):
                    null_symb.add(label)

    result = task3.FiniteAutomaton(m, start_states, final_states, states_map)
    result.epsilon_symbol = null_symb
    result.number_of_states = ls

    graph_matrix = task3.nfa_to_mat(graph_to_nfa(graph, start_nodes, final_nodes))
    mat = result
    graph_matrix_inds = graph_matrix.indices_dict()
    mat_idx = mat.indices_dict()

    n = graph_matrix.size()

    for var in mat.epsilon_symbol:
        if var not in graph_matrix.transitions:
            graph_matrix.transitions[var] = dok_matrix((n, n), dtype=bool)
        graph_matrix.transitions[var] += scipy.sparse.eye(n, dtype=bool)

    last = 0
    cur = None
    while cur != last:
        last = cur
        closure = task3.transitive_closure(
            task3.intersect_automata(mat, graph_matrix)
        ).nonzero()
        closure = list(zip(*closure))
        cur = len(closure)

        for i, j in closure:
            s = mat_idx[i // n]
            d = mat_idx[j // n]

            if s in mat.start_states and d in mat.final_states:
                var = s.value[0]
                if var not in graph_matrix.transitions:
                    graph_matrix.transitions[var] = dok_matrix((n, n), dtype=bool)
                graph_matrix.transitions[var][i % n, j % n] = True

    result = set()
    for _, matrix in graph_matrix.transitions.items():
        non_zero_indices = matrix.nonzero()
        for i, j in zip(*non_zero_indices):
            if (
                graph_matrix_inds[i] in mat.start_states
                and graph_matrix_inds[j] in mat.final_states
            ):
                result.add((graph_matrix_inds[i], graph_matrix_inds[j]))

    return result
