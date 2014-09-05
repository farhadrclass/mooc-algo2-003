"""
    clustering.py
    ~~~~~~~~~~~~

"""

from collections import defaultdict


class UnionFind(object):

    """Implements UnionFind datastructure supporting the following operations:
        - find in O(1) time
        - union in O(logV) time, where V is # vertices
    """

    def __init__(self, nodes=[]):
        """Inits leader and set lookup dictionaries:
            leader_lookup  - { node : leader node }
            set_lookup - { leader node : list of nodes in leader node's set }
        """
        self.leader_lookup = {node: node for node in nodes}
        self.set_lookup = {node: [node] for node in nodes}
    pass

    def union(leader1, leader2):
        "Merges the sets of leader1 and leader 2, taking the new leader to be the larger of the two"
        size_leader1 = len(self.set_lookup[leader1])
        size_leader2 = len(self.set_lookup[leader2])

        (new_leader, old_leader) = (leader1, leader2) if size_leader1 >= size_leader2 else (leader2, leader1)

        old_set = self.set_lookup[old_leader]
        self.set_lookup[new_leader].append(old_set)

        for node in old_set:
            self.leader_lookup[node] = new_leader

    def find(node):
        "Return the leader node which 'node' points to."
        return self.leader_lookup[node]


def kruskal(graph):
    mst = defaultdict(dict)  # minimum spanning tree
    return mst
