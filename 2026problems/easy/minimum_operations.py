"""
You are given an integer array nums and an integer k. You can perform the following operation any number of times:

Select an index i and replace nums[i] with nums[i] - 1.
Return the minimum number of operations required to make the sum of the array divisible by k.
"""


def min_operations(nums, k):
    count = 0
    sum_num = sum(nums)
    for i in range(0, k):
        if sum_num % k == 0:
            return count
        sum_num -= 1
        count += 1


if __name__ == '__main__':
    li = [3,2]
    k = 6
    print(min_operations(li, k))