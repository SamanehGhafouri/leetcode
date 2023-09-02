"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.
"""
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) == 0:
        return [[]]
    if len(strs) == 1:
        return [[strs[0]]]
    result = {}
    for w in strs:
        sorted_w = "".join(sorted(w))
        if sorted_w not in result:
            result[sorted_w] = [w]
        else:
            result[sorted_w].append(w)
    return list(result.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))
