"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of
students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
"""
from typing import List


def num_busy_student(start_time: List[int], end_time: List[int], query_time: int) -> int:
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


if __name__ == '__main__':
    s_time = [1, 2, 3]
    e_time = [3, 2, 7]
    q_time = 4
    print(num_busy_student(s_time, e_time, q_time))
