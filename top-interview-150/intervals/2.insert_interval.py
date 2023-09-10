"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an
interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if len(intervals) == 0:
        intervals.append(newInterval)
        return intervals
    intervals.append(newInterval)
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
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(insert(intervals, newInterval))