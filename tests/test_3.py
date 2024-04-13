from networkx import MultiDiGraph
from task3 import paths_ends


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
