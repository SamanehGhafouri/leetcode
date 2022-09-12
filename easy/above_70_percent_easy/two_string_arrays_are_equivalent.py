"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""
from typing import List


def arrays_strings_are_equal(word1: List[str], word2: List[str]) -> bool:
    word1_str = "".join(word1)
    word2_str = "".join(word2)
    return word1_str == word2_str


if __name__ == '__main__':
    word1_li = ["ab", "c"]
    word2_li = ["a", "bc"]
    print(arrays_strings_are_equal(word1_li, word2_li))
