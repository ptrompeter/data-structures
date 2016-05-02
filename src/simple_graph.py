# _*_ Coding: utf-8 _*_
from stacks import Stack
from queue import Queue
import heapq


class Graph(object):
    """Create a directed, unweighted graph object."""

    def __init__(self):
        """Initialize Graph."""
        self.dict = {}

    def nodes(self):
        """Return a list of all nodes in graph."""
        return list(self.dict.keys())

    def edges(self):
        """Return list of all edges in graph."""
        return_list = []
        for n1 in self.dict.keys():
            for n2 in self.dict[n1]:
                return_list.append((n1, n2))
        return return_list

    def add_node(self, n):
        """Take a node, add to self.dict."""
        self.dict[n] = {}

    def add_edge(self, n1, n2, weight=1):
        """Add edge between nodes in graph.

        If nodes not in graph, add them. Default weight of one.
        """
        if n1 not in self.dict:
            self.add_node(n1)
        if n2 not in self.dict:
            self.add_node(n2)
        self.dict[n1][n2] = weight

    def del_node(self, n):
        """Delete Node."""
        for key in self.dict.keys():
            if n in key:
                key.remove(n)
        del self.dict[n]

    def del_edge(self, n1, n2):
        """Delete edge between nodes."""
        self.dict[n1].pop(n2)

    def has_node(self, n):
        """Return boolean value representing nodes presence in graph."""
        return True if n in self.dict.keys() else False

    def neighbors(self, n):
        """Return all neighbors of node."""
        return self.dict[n]

    def adjacent(self, n1, n2):
        """Return boolean value representing if two nodes are adjacent."""
        if n2 in self.dict[n1]:
            return True
        raise ValueError

    def depth_first_traversal(self, start):
        """Traverse graph depth first."""
        depth_list = []
        new_stack = Stack([start])
        while True:
            try:
                node = new_stack.pop()
                if node not in depth_list:
                    depth_list.append(node)
                    children = list(self.dict[node].keys())

                    for child in children:
                        new_stack.push(child)

            except AttributeError:
                return depth_list

    def breadth_first_traversal(self, start):
        """Traverse graph breadth first."""
        breadth_list = []
        new_queue = Queue()
        new_queue.enqueue(start)
        while not new_queue.is_empty:
            node = new_queue.dequeue()
            if node not in breadth_list:
                breadth_list.append(node)
                for child in self.dict[node]:
                    new_queue.enqueue(child)
        return breadth_list

    def dijkstra(self, start, end):
        """Implementation of Dijkstra's shortest path algorithm."""
        from itertools import count
        unique = count()
        visited = set()
        heap = [(0, unique, start, ())]
        while heap:
            weight, junk, node, path = heapq.heappop(heap)
            if node == end:
                return weight, path
            if node not in visited:
                visited.add(node)
                for neighbor, edge in self.dict[node].items():
                    heapq.heappush(heap, (weight + edge, next(unique), neighbor, (neighbor, path)))

    def floyd(self):
        """Implementation of Floyd-Warshall's shortest path algorithm."""
        dist = {}
        for n1 in self.dict:
            dist[n1] = {}
            dist[n1][n1] = 0
        for n1 in dist:
            for n2 in dist:
                try:
                    dist[n1][n2] = self.dict[n1][n2]
                except KeyError:
                    pass
        for k in self.dict:
            for i in self.dict:
                for j in self.dict:
                    try:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
                    except KeyError:
                        pass
        return dist
