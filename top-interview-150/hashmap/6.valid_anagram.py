"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using
all the original letters exactly once.
"""
import collections


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dict_s = collections.Counter(s)
    dict_t = collections.Counter(t)
    return dict_s == dict_t


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(is_anagram(s, t))
