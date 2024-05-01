import networkx as nx
from pyformlang.cfg import Epsilon
from pyformlang.finite_automaton import State, Symbol
from pyformlang.regular_expression import Regex
from pyformlang.rsa import Box
from scipy.sparse import dok_matrix, eye
from pyformlang.cfg import CFG
from pyformlang.rsa import RecursiveAutomaton
from project.task2 import graph_to_nfa
from project.task3 import (
    FiniteAutomaton,
    nfa_to_matrix,
    transitive_closure,
    intersect_automata,
)


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
    rsm: RecursiveAutomaton,
    graph: nx.MultiDiGraph,
    final_nodes: set[int] = None,
    start_nodes: set[int] = None,
) -> set[tuple[int, int]]:
    rsm_mat, _ = rsm_to_matrix(rsm)
    graph_mat = nfa_to_matrix(graph_to_nfa(graph, start_nodes, final_nodes))

    num_states = graph_mat.size()
    last_nnz: int = 0

    while True:
        closure = transitive_closure(intersect_automata(rsm_mat, graph_mat)).nonzero()
        closure = list(zip(*closure))

        nnz_count = len(closure)
        if nnz_count == last_nnz:
            break
        last_nnz = nnz_count

        for i, j in closure:
            src = rsm_mat.mapping_for(i)
            dst = rsm_mat.mapping_for(j)

            if src in rsm_mat.start and dst in rsm_mat.final:
                var = rsm_mat.indexes_dict()[i].value[0]
                if var not in graph_mat.m:
                    graph_mat.m[var] = dok_matrix((num_states, num_states), dtype=bool)
                graph_mat.m[var][i, j] = True

    result: set[tuple[int, int]] = set()
    for _, m in graph_mat.m.items():
        for i, j in zip(*m.nonzero()):
            if (
                graph_mat.indexes_dict()[i] in rsm_mat.start
                and graph_mat.indexes_dict()[j] in rsm_mat.final
            ):
                result.add((graph_mat.indexes_dict()[i], graph_mat.indexes_dict()[j]))

    return result

def rsm_to_matrix(rsm: RecursiveAutomaton) -> tuple:
    all_states = set()
    start_states = set()
    final_states = set()
    epsilon_symbols = set()

    for var, p in rsm.boxes.items():
        for state in p.dfa.states:
            s = State((var, state.value))
            all_states.add(s)
            if state in p.dfa.start_states:
                start_states.add(s)
            if state in p.dfa.final_states:
                final_states.add(s)

    mapping = {v: i for i, v in enumerate(sorted(all_states, key=lambda x: x.value[1]))}

    m = {}

    for var, p in rsm.boxes.items():
        for src, transition in p.dfa.to_dict().items():
            for symbol, dst in transition.items():
                label = symbol.value
                if label not in m:
                    m[label] = dok_matrix(
                        (len(all_states), len(all_states)), dtype=bool
                    )
                for target in {dst} if not isinstance(dst, set) else dst:
                    m[label][
                        mapping[State((var, src.value))],
                        mapping[State((var, target.value))],
                    ] = True
                if isinstance(dst, Epsilon):
                    epsilon_symbols.add(label)

    result = FiniteAutomaton(m, start_states, final_states, mapping)
    result.states_count = len(all_states)

    return result, epsilon_symbols
