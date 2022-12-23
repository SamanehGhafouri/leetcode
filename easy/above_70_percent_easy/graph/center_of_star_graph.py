"""
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is
one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the
nodes ui and vi. Return the center of the given star graph.
"""
import collections
from typing import List


def center_of_star(edges: List[List[int]]) -> int:
    adj_list = collections.defaultdict(set)
    for i, j in edges:
        adj_list[i].add(j)
        adj_list[j].add(i)

    for k, v in adj_list.items():
        if len(v) > 1:
            return k
    return -1


if __name__ == '__main__':
    edgs = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(center_of_star(edgs))
