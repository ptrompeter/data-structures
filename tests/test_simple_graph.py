# _*_ Coding: utf-8 _*_

import pytest
# from src.simple_graph import Node
from src.simple_graph import Graph

# TEST_NODE_1 = Node(1)
# TEST_NODE_2 = Node(2)

TEST_GRAPH = Graph()
TEST_GRAPH.add_edge('a', 'b')
TEST_GRAPH.add_edge('a', 'c')
TEST_GRAPH.add_edge('a', 'd')
TEST_GRAPH.add_edge('b', 'e')
TEST_GRAPH.add_edge('b', 'f')
TEST_GRAPH.add_edge('c', 'g')

HARD_GRAPH = Graph()
HARD_GRAPH.add_edge(1, 7)
HARD_GRAPH.add_edge(1, 13)
HARD_GRAPH.add_edge(1, 3)
HARD_GRAPH.add_edge(7, 11)
HARD_GRAPH.add_edge(11, 13)
HARD_GRAPH.add_edge(13, 7)
HARD_GRAPH.add_edge(13, 11)
HARD_GRAPH.add_edge(13, 3)
HARD_GRAPH.add_edge(3, 2)

def test_dijkstra_1():
    assert HARD_GRAPH.dijkstra(1,2)[0] == 2

def test_dijkstra_2():
    assert HARD_GRAPH.dijkstra(13,1) == None

def test_sgraph_wide():
    # assert TEST_GRAPH.breadth_first_traversal('a') == ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    traversal = TEST_GRAPH.breadth_first_traversal('a')
    assert traversal.index('e') > traversal.index('d')
    assert traversal.index('f') > traversal.index('d')
    assert traversal.index('g') > traversal.index('d')
    assert traversal.index('e') > traversal.index('c')
    assert traversal.index('f') > traversal.index('c')
    assert traversal.index('g') > traversal.index('c')
    assert traversal.index('e') > traversal.index('b')
    assert traversal.index('f') > traversal.index('b')
    assert traversal.index('g') > traversal.index('b')
    assert traversal[-1] in ['e', 'f', 'g']
    assert traversal[0] == 'a'



def test_sgraph_deep():
    # assert TEST_GRAPH.depth_first_traversal('a') == ['a', 'b', 'e', 'f', 'c', 'g', 'd']
    traversal = TEST_GRAPH.depth_first_traversal('a')
    assert traversal.index('g') == traversal.index('c') + 1
    assert traversal[traversal.index('b') + 1] in ['e', 'f'] 
    assert abs(traversal.index('e') - traversal.index('f')) == 1




def test_sgraph_deep2():
    # assert HARD_GRAPH.depth_first_traversal(1) == [1, 7, 11, 13, 3, 2]
    traversal = HARD_GRAPH.depth_first_traversal(1)
    assert traversal[traversal.index(11) -1] in [7, 13]
    assert traversal.index(2) == traversal.index(3) + 1
    assert traversal[2] in [2,3,11]
    assert traversal[-1] in [7, 11, 2]


def test_sgraph_wide2():
    # assert HARD_GRAPH.breadth_first_traversal(1) == [1, 7, 13, 3, 11, 2]
    traversal = HARD_GRAPH.breadth_first_traversal(1)
    assert traversal.index(11) > traversal.index(7)
    assert traversal.index(11) > traversal.index(13)
    assert traversal.index(11) > traversal.index(3)
    assert traversal.index(2) > traversal.index(7)
    assert traversal.index(2) > traversal.index(13)
    assert traversal.index(2) > traversal.index(3)
    assert traversal.index(3) < 4
    assert traversal.index(7) < 4
    assert traversal.index(13) < 4
    assert traversal[-1] == 2 or traversal[-1] == 11
    assert traversal[0] == 1


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
    assert test_graph.dict[2] == {}
    

def test_sgraph_add_edge():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_node(3)
    test_graph.add_edge(2,3,5)
    assert test_graph.dict[2] == {3:5}

def test_sgraph_add_edge_add_n2():
    from src.simple_graph import Graph
    test_graph = Graph()
    test_graph.add_node(2) 
    test_graph.add_edge(2,3)
    assert test_graph.dict[2] == {3:1}

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
    assert test_graph.neighbors(2) == {3:1,4:1}

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
