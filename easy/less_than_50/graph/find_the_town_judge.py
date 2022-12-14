"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
"""
import collections
from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:
    adj_list = collections.defaultdict(set)
    for i, j in trust:
        adj_list[i].add(j)

    possible_judges = []
    for i in range(1, n + 1):
        if i not in adj_list:
            possible_judges.append(i)

    count = 0
    possible_judge_and_count = {}
    for j in possible_judges:
        for k, v in adj_list.items():
            if j in v:
                count += 1
        possible_judge_and_count[j] = count
        count = 0

    if len(possible_judge_and_count) == 0:
        return -1

    for k, v in possible_judge_and_count.items():
        if v == (n - 1):
            result = k
        else:
            result = -1
        return result


if __name__ == '__main__':
    n = 3
    trust = [[1, 3], [2, 3]]
    print(find_judge(n, trust))
