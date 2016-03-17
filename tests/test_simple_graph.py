# _*_ Coding: utf-8 _*_

import pytest
from src.simple_graph import Node

TEST_NODE_1 = Node(1)
TEST_NODE_2 = Node(2)


def test_sgraph_nodes():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    assert test_graph.nodes() == [2]


def test_sgraph_edges():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_node(3)
    test_graph.add_node(4)
    test_graph.add_edge(2,3)
    test_graph.add_edge(2,4)
    assert test_graph.edges() == [(2,3), (2,4)]


def test_sgraph_add_node():
    #expect new entry in dict
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    assert test_graph.dict[2] == []
    

def test_sgraph_add_edge():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_node(3)
    test_graph.add_edge(2,3)
    assert test_graph.dict[2] == [3]

def test_sgraph_add_edge_add_n2():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_edge(2,3)
    assert test_graph.dict[2] == [3]

def test_sgraph_add_edge_added_key():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_edge(2,3)
    assert 3 in test_graph.nodes()

def test_sgraph_add_edge_no_nodes():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_edge(2,3)
    assert 3 in test_graph.nodes() and 2 in test_graph.nodes()

def test_sgraph_del_node():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_edge(2,3)

def test_sgraph_del_node_empty():
    from src.simple_graph import Graph
    test_graph = Graph()
    with pytest.raises(KeyError):
        test_graph.del_node(2)

def test_sgraph_del_edge():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_edge(2,3)
    test_graph.add_edge(2,4)
    test_graph.del_edge(2, 3)
    assert (2,3) not in test_graph.edges()

def test_sgraph_del_edge_empty():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2)
    test_graph.add_node(3)
    with pytest.raises(KeyError):
        test_graph.del_edge(2, 3)

def test_sgraph_has_node():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_edge(2,3)
    assert test_graph.has_node(2)

def test_sgraph_neighbors():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_edge(2,3)
    test_graph.add_edge(2,4)
    assert test_graph.neighbors(2) == [3,4]

def test_sgraph_neighbors_error():
    from src.simple_graph import Graph
    test_graph = Graph()
    with pytest.raises(KeyError):
        test_graph.neighbors(2)

def test_sgraph_adjacent():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_edge(2,3)
    assert test_graph.adjacent(2,3)
