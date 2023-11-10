"""
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

The company requires each employee to work for at least target hours.

You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

Return the integer denoting the number of employees who worked at least target hours.
"""
from typing import List


def number_of_employee_met_target(hours: List[int], target: int) -> int:
    count = 0
    for h in hours:
        if h >= target:
            count += 1
    return count


if __name__ == '__main__':
    hours = [0, 1, 2, 3, 4]
    t = 2
    print(number_of_employee_met_target(hours, t))
