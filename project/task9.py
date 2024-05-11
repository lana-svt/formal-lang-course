import networkx as nx
from scipy.sparse import dok_matrix
from pyformlang.rsa import RecursiveAutomaton
from project.task2 import graph_to_nfa
from project.task3 import (
    nfa_to_matrix,
    transitive_closure,
    intersect_automata,
)
from project.task8 import rsm_to_matrix


def cfpq_with_gll(
        rsm: RecursiveAutomaton,
        graph: nx.DiGraph,
        start_nodes: set[int] = None,
        final_nodes: set[int] = None,
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
