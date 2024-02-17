"""
There is a class with m students and n exams. You are given a 0-indexed m x n integer matrix score, where each row
represents one student and score[i][j] denotes the score the ith student got in the jth exam. The matrix score
contains distinct integers only.

You are also given an integer k. Sort the students (i.e., the rows of the matrix) by their scores in
the kth (0-indexed) exam from the highest to the lowest.

Return the matrix after sorting it.
"""
from typing import List


def sort_the_students(score: List[List[int]], k) -> List[List[int]]:
    kth_scores = []
    result = [[] for _ in range(len(score))]

    for i in range(len(score)):
        for j in range(len(score[i])):
            if j == k:
                kth_scores.append([score[i][j], i])

    kth_scores.sort()
    i = 0
    while kth_scores:
        s, ith = kth_scores.pop()
        result[i].extend(score[ith])
        i += 1
    return result


if __name__ == '__main__':
    score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k = 2
    print(sort_the_students(score, k))
