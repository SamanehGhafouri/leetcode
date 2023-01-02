"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible
paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node
i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
from typing import List


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    start = 0
    target = len(graph) - 1
    stack = [(start, [start])]
    result = []
    while stack:
        node, path = stack.pop()
        if node == target:
            result.append(path)
        else:
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))
    return result


if __name__ == '__main__':
    data = [
        ([[4, 3, 1], [3, 2, 4], [3], [4], []], [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]),
        ([[1, 2], [3], [3], []], [[0, 1, 3], [0, 2, 3]])
    ]
    for d in data:
        print(f"actual = {all_paths_source_target(d[0])}", f"expected = {d[1]}")
