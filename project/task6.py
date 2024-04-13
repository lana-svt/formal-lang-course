import pyformlang
from typing import Set, Tuple
from pyformlang.cfg import *
import networkx as nx


def cfg_to_weak_normal_form(cfg: pyformlang.cfg.CFG) -> pyformlang.cfg.CFG:
    cfg = cfg.eliminate_unit_productions().remove_useless_symbols()

    new_productions = cfg._get_productions_with_only_single_terminals()
    new_productions = cfg._decompose_productions(new_productions)

    return CFG(
        start_symbol=cfg.start_symbol,
        productions=set(new_productions),
    )


def extract(g):
    k_1, k_2, k_3 = {}, set(), {}


    for p in g.productions:
        if len(p.body) == 1 and isinstance(p.body[0], Terminal):
            k_1.setdefault(p.head, set()).add(p.body[0])
        elif len(p.body) == 1 and isinstance(p.body[0], Epsilon):
            k_2.add(p.body[0])
        elif len(p.body) == 2:
            k_3.setdefault(p.head, set()).add((p.body[0], p.body[1]))

    return k_1, k_2, k_3


def extract_r(cfg, graph, p1, p2):
    r = {(N_i, v, v) for N_i in p2 for v in graph.nodes}
    r |= {
        (N_i, v, u)
        for (v, u, tag) in graph.edges.data("label")
        for N_i in p1
        if tag in p1[N_i]
    }
    return r


def compute_r(m, r, p3):
    while len(m) > 0:
        N_i, v, u = m.pop()

        r_tmp = set()
        for N_j, v_, u_ in r:
            if v == u_:
                for N_k in p3:
                    if (N_j, N_i) in p3[N_k] and (N_k, v_, v) not in r:
                        m.add((N_k, v_, u))
                        r_tmp.add((N_k, v_, u))
        r |= r_tmp
    return r


def filter_results(r, start_nodes, final_nodes, cfg):
    filtered_results = set()
    for N_i, v, u in r:
        if v in start_nodes and u in final_nodes and Variable(N_i) == cfg.start_symbol:
            filtered_results.add((v, u))
    return filtered_results


def cfpq_with_hellings(
    cfg: CFG,
    graph: nx.DiGraph,
    start_nodes: Set[int] = None,
    final_nodes: Set[int] = None,
) -> Set[Tuple[int, int]]:
    if start_nodes is None:
        start_nodes = graph.nodes
    if final_nodes is None:
        final_nodes = graph.nodes

    g = cfg_to_weak_normal_form(cfg)
    k_1, k_2, k_3 = extract(g)

    r = extract_r(cfg, graph, k_1, k_2)

    m = r.copy()

    r = compute_r(m, r, k_3)

    filtered_results = filter_results(r, start_nodes, final_nodes, cfg)
    return filtered_results
