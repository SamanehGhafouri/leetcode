"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""
import heapq


def find_kth_largest_element(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


#####################################################################################################

def find_kth_largest_element_second_solution(nums, k):
    return sorted(nums)[-k]


######################################################################################################
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def sift_down(lst, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i, r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i, l)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst, i, r)
                i = r
            else:
                break
        else:
            break


def heapsort(lst):
    for j in range((len(lst) - 2) // 2, -1, -1):
        sift_down(lst, j, len(lst))
    for end in range(len(lst) - 1, 0, -1):
        swap(lst, 0, end)
        sift_down(lst, 0, end)
    return lst


if __name__ == '__main__':
    lst = [3, 2, 1, 5, 6, 4]
    print(find_kth_largest_element(lst, 4))
