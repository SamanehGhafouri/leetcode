"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums
such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.
"""
from typing import List


def answer_queries(nums: List[int], queries: List[int]) -> List[int]:
    nums.sort()
    answer = []
    for q in queries:
        sum_nums = 0
        count_num = 0
        for n in nums:
            if sum_nums >= q:
                break
            sum_nums += n
            count_num += 1
        if sum_nums > q:
            answer.append(count_num - 1)
        else:
            answer.append(count_num)
    return answer


if __name__ == '__main__':
    nums = [4,5,2,1]
    queries = [3,10,21]
    print(answer_queries(nums, queries))