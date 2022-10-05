"""
There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges
that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that
there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""
from typing import List


def find_center(edges: List[List[int]]) -> int:
    # you only need to check the intersection of the first two edges in edges list to get the common element.
    # Because the center of the graph (node) exists in each edge.
    return set(edges[0]).intersection(set(edges[1])).pop()


if __name__ == '__main__':
    edges_list = [[1, 2], [5, 1], [1, 3], [1, 4]]
    print(find_center(edges_list))
