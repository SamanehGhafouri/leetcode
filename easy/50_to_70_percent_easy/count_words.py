"""
Given two string arrays words1 and words2, return the number of
 strings that appear exactly once in each of the two arrays.
"""
import collections
from typing import List


def count_words(words1: List[str], words2: List[str]) -> int:
    dict_words1 = collections.Counter(words1)
    dict_words2 = collections.Counter(words2)

    count = 0
    for key, val in dict_words1.items():
        if val == 1 and key in dict_words2 and dict_words2[key] == 1:
            count += 1
    return count


if __name__ == '__main__':
    arr1 = ["a", "ab"]
    arr2 = ["a", "a", "a", "ab"]
    # arr1 = ["leetcode", "is", "amazing", "as", "is"]
    # arr2 = ["amazing", "leetcode", "is"]
    print(count_words(arr1, arr2))
