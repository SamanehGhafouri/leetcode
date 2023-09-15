"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
import collections


def find_unique_chr(s: str) -> int:
    dict_ch = collections.Counter(s)
    for ch in s:
        if dict_ch[ch] == 1:
            return s.index(ch)
    return -1


if __name__ == '__main__':
    items = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1)
    ]
    for item in items:
        print(item[1] == find_unique_chr(item[0]))
