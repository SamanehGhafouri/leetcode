"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    merged = [intervals[0]]
    for interval in intervals[1::]:
        last_interval = merged[-1]
        if interval[0] <= last_interval[1]:
            if last_interval[1] < interval[1]:
                merged.pop()
                merged.append([last_interval[0], interval[1]])
        else:
            merged.append(interval)
    return merged


if __name__ == '__main__':
    inputs = [[1, 3], [2, 6], [8, 10], [15, 18], [1, 1]]
    print(merge(inputs))
