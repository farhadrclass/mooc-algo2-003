from collections import defaultdict
from union_find import UnionFind
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
