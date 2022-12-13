"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from
source to destination, or false otherwise.
"""
from typing import List
from collections import defaultdict


def valid_path(n:int, edges:List[List[int]], source:int, destination:int) -> bool:
    if n == 1 and source == destination:
        return True

    adj_li = defaultdict(set)
    for i, j in edges:
        adj_li[i].add(j)
        adj_li[j].add(i)

    visited = set()
    stack = [source]
    while len(stack) > 0:
        node = stack.pop()
        visited.add(node)
        children = adj_li[node]
        for child in children:
            if child == destination:
                return True
            if child not in visited:
                stack.append(child)
    return False


if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[2,0]]
    source = 0
    destination = 2
    print(valid_path(n, edges, source, destination))