from typing import List


class BinarySearch:

    def binary_search(self, nums: List[int], target, low, high) -> int:
        if high >= low:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return self.binary_search(nums, target, low, mid - 1)
            else:
                return self.binary_search(nums, target, mid + 1, high)
        else:
            return False


if __name__ == '__main__':
    obj = BinarySearch()
    arr = [2, 5, 6, 8, 10, 12, 14, 16]
    print(obj.binary_search(arr, 15, 0, len(arr)))
