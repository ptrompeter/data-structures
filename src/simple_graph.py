# _*_ Coding: utf-8 _*_
class Node(object):
    def __init__(self, data):
        self.data = data

class Graph(object):
    """Create a directed, unweighted graph object."""

    def __init__(self):
        self.dict = {}

    def nodes(self):
        return list(self.dict.keys())

    def edges(self):
        #use itertools
        return_list = []
        for n1 in self.dict.keys():
            for n2 in self.dict[n1]:
                return_list.append((n1, n2))
        return return_list


    def add_node(self, n):
        """Take a node, add to self.dict"""
        self.dict[n] = []

    def add_edge(self, n1, n2):
        if n1 not in self.dict:
            self.add_node(n1)
        if n2 not in self.dict:
            self.add_node(n2)
        self.dict[n1].append(n2)

    def del_node(self, n):
        for key in self.dict.keys():
            if n in keys:
                keys.remove(n)
        del self.dict[n]

    def del_edge(self, n1, n2):
        if n2 in self.dict[n1]:
            self.dict[n1].remove(n2)
        else: raise KeyError

    def has_node(self, n):
        return True if n in self.dict.keys() else False

    def neighbors(self, n):
        return self.dict[n]

    def adjacent(self, n1, n2):
        return True if n2 in self.dict[n1] else False
