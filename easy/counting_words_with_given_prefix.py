"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.
"""
from typing import List


def prefix_count(words: List[str], pref: str) -> int:
    count = 0
    for word in words:
        if word[:len(pref)] == pref:
            count += 1
    return count


if __name__ == '__main__':
    words_arr = ["leetcode", "win", "loops", "success"]
    prefix = "at"
    print(prefix_count(words_arr, prefix))
