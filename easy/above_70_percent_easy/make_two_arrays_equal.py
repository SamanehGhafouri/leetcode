"""
You are given two integer arrays of equal length target and arr. In one step, you can select
any non-empty sub-array of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.
"""
from typing import List


def can_be_equal(target: List[int], arr: List[int]) -> bool:
    target.sort()
    arr.sort()
    if arr != target:
        return False
    return True


if __name__ == '__main__':
    t = [3, 7, 9]
    ar = [3, 7, 11]
    print(can_be_equal(t, ar))
