"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

from typing import List


def largest_altitude(gain: List[int]) -> int:
    li_altitude = [0, gain[0]]
    count_altitudes = gain[0]
    for altitude in range(len(gain) - 1):
        count_altitudes += gain[altitude + 1]
        li_altitude.append(count_altitudes)
    return max(li_altitude)


if __name__ == '__main__':
    arr_gain = [-5, 1, 5, 0, -7]
    print(largest_altitude(arr_gain))
