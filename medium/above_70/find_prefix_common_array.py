"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or
before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
"""
import collections
from typing import List


def find_prefix_common_array(A: List[int], B: List[int]) -> List[int]:
    set_a = set()
    set_b = set()
    result = [0 for _ in range(len(A))]
    count = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            count += 1
        if A[i] in set_b and B[i] in set_a:
            count += 2
        elif A[i] in set_b and B[i] not in set_a:
            count += 1
            set_a.add(A[i])
            set_b.add(B[i])
        elif A[i] not in set_b and B[i] in set_a:
            count += 1
            set_a.add(A[i])
            set_b.add(B[i])
        set_a.add(A[i])
        set_b.add(B[i])
        result[i] = count
    return result


if __name__ == '__main__':
    A = [1, 3, 2, 4]
    B = [3, 1, 2, 4]
    # A = [2, 3, 1]
    # B = [3, 1, 2]
    print(find_prefix_common_array(A, B))
