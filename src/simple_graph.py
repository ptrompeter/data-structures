# _*_ Coding: utf-8 _*_


class Graph(object):
    """Create a directed, unweighted graph object."""

    def __init__(self):
        """Initialize graph with an empty dictionary to hold nodes."""
        self.dict = {}

    def nodes(self):
        """Return all nodes in graph.

        Wrap in list to keep compatibility with new py3 dict.keys() object.
        """
        return list(self.dict.keys())

    def edges(self):
        """Return list of all edges between nodes in graph."""
        return_list = []
        for n1 in self.dict.keys():
            for n2 in self.dict[n1]:
                return_list.append((n1, n2))
        return return_list

    def add_node(self, n):
        """Take a node, add to self.dict."""
        self.dict[n] = []

    def add_edge(self, n1, n2):
        """Add new edge between two nodes in graph.

        If either node not in graph, add it to the graph.
        """
        if n1 not in self.dict:
            self.add_node(n1)
        if n2 not in self.dict:
            self.add_node(n2)
        self.dict[n1].append(n2)

    def del_node(self, n):
        """Delete node in graph."""
        for key in self.dict.keys():
            if n in self.dict[key]:
                key.remove(n)
        del self.dict[n]

    def del_edge(self, n1, n2):
        """Delete edge in graph."""
        self.dict[n1].remove(n2)

    def has_node(self, n):
        """Determine if node in graph. Return Boolean value."""
        return n in self.dict.keys()

    def neighbors(self, n):
        """Return all neighbors of a node in graph."""
        return self.dict[n]

    def adjacent(self, n1, n2):
        """Determine if edge exists in graph. Return Boolean value."""
        return n2 in self.dict[n1]
