# _*_ Coding: utf-8 _*_
from stacks import Stack
from queue import Queue

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
        self.dict[n] = {}

    def add_edge(self, n1, n2, weight=0):
        if n1 not in self.dict:
            self.add_node(n1)
        if n2 not in self.dict:
            self.add_node(n2)
        self.dict[n1][n2] = weight

    def del_node(self, n):
        for key in self.dict.keys():
            if n in keys:
                keys.remove(n)
        del self.dict[n]

    def del_edge(self, n1, n2):
        self.dict[n1].pop(n2)

    def has_node(self, n):
        return True if n in self.dict.keys() else False

    def neighbors(self, n):
        return self.dict[n]

    def adjacent(self, n1, n2):
        return True if n2 in self.dict[n1] else False

    def depth_first_traversal(self, start):
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


