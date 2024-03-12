from networkx import MultiDiGraph
from project.task3 import paths_ends


def test_paths_ends_complex():
    g = MultiDiGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_edge(0, 1, label="a")
    g.add_edge(1, 2, label="b")
    g.add_edge(2, 0, label="c")

    result = paths_ends(g, {0}, {2}, "a.b.c*")
    assert result == [(0, 2)]


def test_paths_ends_empty_graph():
    g = MultiDiGraph()

    result = paths_ends(g, {0}, {1}, "a")
    assert result == []


def test_paths_ends_no_matching_paths():
    g = MultiDiGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_edge(0, 1, label="b")

    result = paths_ends(g, {0}, {1}, "a")
    assert result == []


def test_paths_ends_self_loop():
    g = MultiDiGraph()
    g.add_node(0)
    g.add_edge(0, 0, label="a")

    result = paths_ends(g, {0}, {0}, "a*")
    assert result == [(0, 0)]


def test_paths_ends_multiple_edges_same_nodes():
    g = MultiDiGraph()
    g.add_node(0)
    g.add_edge(0, 0, label="a")
    g.add_edge(0, 0, label="b")

    result = paths_ends(g, {0}, {0}, "a.b")
    assert result == [(0, 0)]


def test_paths_ends_disjoint_graphs():
    g1 = MultiDiGraph()
    g1.add_node(0)
    g1.add_edge(0, 0, label="a")

    g2 = MultiDiGraph()
    g2.add_node(1)
    g2.add_edge(1, 1, label="b")

    result = paths_ends(g1, {0}, {0}, "a") + paths_ends(g2, {1}, {1}, "b")
    assert result == [(0, 0), (1, 1)]
