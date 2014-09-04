import math
import numpy
import random
from collections import defaultdict


class Node(object):

    def __init__(self, key=None, name=None):
        self._pos = float("inf")
        self._key = key
        self._name = name

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def __repr__(self):
        return self.key

    def __str__(self):
        return "Name: {}, Key: {}".format(self.name, self.key)

    def __lt__(self, other):
        return self.key < other.key

    def __eq__(self, other):
        return all([getattr(self, var) == getattr(other, var) for var in vars(self)])


class Heap(object):

    def __init__(self, array=[], mode='min', named=True):
        self._node_array = [Node(key=node[0], name=node[1])
                            for node in array]  # contains Nodes
        self._node_lookup = {}  # enable node position lookup
        self.mode = mode
        self.named = named

        self.heapify()

    @property
    def node_array(self):
        return self._node_array

    @node_array.setter
    def node_array(self, value):
        self._node_array = value

    @property
    def node_lookup(self):
        return self._node_lookup

    @node_lookup.setter
    def node_lookup(self, value):
        self._node_lookup = value

    def __getitem__(self, key):
        return self.node_array[self._node_lookup[key]]

    def __len__(self):
        return len(self.array)

    def __str__(self):
        return str(self.node_keys())

    def heapify(self):
        self.node_array = sorted(self.node_array, key=lambda node: node.key)
        if self.mode == 'max':
            self.node_array = reversed(self.node_array)

        for index, node in enumerate(self.node_array):
            node.pos = index
            self.node_array[index] = node
            self.node_lookup[node.name] = node.pos

    def insert(self, node):
        node.pos = len(self.node_array)
        self.node_array.append(node)
        self.bubble_up(node.pos)
        pass

    def update_key(self, node, key):
        node.key = key
        self.bubble_up(node)
        self.bubble_down(node)

    def delete(self, node):

        if node != self.node_array[-1]:
            original_pos = node.pos
            self.swap_nodes(node, self.node_array[-1])
            self.node_array.pop()
            self.bubble_down(original_pos)
        else:
            self.node_array.pop()


    def pop(self):
        node = self.node_array[0]
        self.delete(node)
        return node

    def node_names(self):
        return self.node_lookup.keys()

    def node_keys(self):
        return [node.key for node in self.node_array]


    def swap_nodes(self, node1, node2):
        node1.pos, node2.pos = node2.pos, node1.pos
        self.node_array[node1.pos], self.node_array[node2.pos] = node1, node2
        self.node_lookup[node1.name], self.node_lookup[
            node2.name] = node1.pos, node2.pos

    def bubble_up(self, child_pos=None):
        if child_pos is None:
            child_pos = len(self.node_array) - 1

        child_node = self.node_array[child_pos]
        while child_node.pos > 0:
            parent_pos = (child_node.pos+1) // 2 - 1
            parent_node = self.node_array[parent_pos]

            if child_node.key <= parent_node.key:
                self.swap_nodes(child_node, parent_node)
                continue
            else:
                break

    def bubble_down(self, parent_pos=0):
        max_num_parents = self.max_num_parents()
        parent_node = self.node_array[parent_pos]
        while parent_node.pos < max_num_parents:
            children = self.get_children(parent_node)

            if all(parent_node.key < child_node.key for child_node in children):
                break
            elif len(children) == 1:
                self.swap_nodes(parent_node, children[0])
            elif len(children) == 2:
                self.swap_nodes(parent_node, min(children))

    def max_num_parents(self):
        return int(math.pow(2, math.floor(math.log(len(self.node_array), 2))) - 1)

    def get_children(self, parent_node):
        parent_pos = parent_node.pos
        left_child_pos = (parent_pos + 1) * 2 - 1
        right_child_pos = (parent_pos + 1) * 2

        children_nodes = []
        for pos in [left_child_pos, right_child_pos]:
            try:
                children_nodes.append(self.node_array[pos])
            except IndexError:
                pass

        return children_nodes

    def is_heap_property_satisfied(self):
        for parent_pos in xrange(0, self.max_num_parents()):
            parent_node = self.node_array[parent_pos]
            children_nodes = self.get_children(parent_node)
            if self.mode == 'min':
                for child_node in children_nodes:
                    if parent_node > child_node:
                        return False
        else:
            return True
