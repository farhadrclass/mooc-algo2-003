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

    @property
    def leader_lookup(self):
        return self._leader_lookup
    @leader_lookup.setter
    def leader_lookup(self, value):
        self._leader_lookup = value

    @property
    def set_lookup(self):
        return self._set_lookup
    @set_lookup.setter
    def set_lookup(self, value):
        self._set_lookup = value



    def union(self, node1, node2):
        "Merges the sets of leader1 and leader 2, taking the new leader to be the larger of the two"
        leader1 = self.leader_lookup[node1]
        leader2 = self.leader_lookup[node2]

        size_leader1 = len(self.set_lookup[leader1])
        size_leader2 = len(self.set_lookup[leader2])

        (new_leader, old_leader) = (leader1, leader2) if size_leader1 >= size_leader2 else (leader2, leader1)

        old_set = self.set_lookup.pop(old_leader, [])
        self.set_lookup[new_leader] += old_set

        for node in old_set:
            self.leader_lookup[node] = new_leader

    def find(self, node):
        "Return the leader node which 'node' points to."
        return self.leader_lookup[node]


def kruskal(node_list, edge_list):
    edge_list.sort()
    mst = defaultdict(dict)  # minimum spanning tree
    union_find = UnionFind(nodes=node_list)
    for edge in edge_list:
        weight, node1, node2 = edge
        if union_find.find(node1) != union_find.find(node2):
            union_find.union(node1, node2)
            mst[node1][node2] = weight
            mst[node2][node1] = weight
        else:
            continue
    return mst
