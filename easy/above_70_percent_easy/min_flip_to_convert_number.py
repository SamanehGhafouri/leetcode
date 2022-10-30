"""
A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from
either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any
leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the
second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
"""


def min_bit_filips(start: int, goal: int) -> int:
    binary_start = bin(start)[2:]
    binary_goal = bin(goal)[2:]
    diff = abs(len(binary_goal) - len(binary_start))
    if len(binary_goal) >= len(binary_start):
        max_num = binary_goal
        min_num = binary_start
    if len(binary_goal) < len(binary_start):
        max_num = binary_start
        min_num = binary_goal

    list_zero_min_num_needs = []
    for _ in range(diff):
        list_zero_min_num_needs.append("0")
    new_min = "".join(list_zero_min_num_needs) + min_num

    count = 0
    for bit in range(len(max_num)):
        if max_num[bit] != new_min[bit]:
            count += 1
    return count


if __name__ == '__main__':
    s = 10
    g = 7
    print(min_bit_filips(s, g))
