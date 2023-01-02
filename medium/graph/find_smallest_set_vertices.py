"""
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array
edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
"""
from typing import List
from collections import defaultdict


def find_smallest_set_of_vertices(n: int, edges: List[List[int]]) -> List[int]:
    adj_list = defaultdict(set)
    for i, j in edges:
        adj_list[i].add(j)

    set_vs = set()
    vertices = set([i for i in range(0, n)])
    for key, value in adj_list.items():
        if key in vertices:
            set_vs.add(key)
        for v in value:
            if v in vertices:
                vertices.remove(v)
    return list(vertices.intersection(set_vs))


if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    print(find_smallest_set_of_vertices(n, edges))
