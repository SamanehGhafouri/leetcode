"""
You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.
Return the number of strings in words that are a prefix of s.
A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous
sequence of characters within a string.
"""

from typing import List


def count_prefixes(words: List[str], s: str) -> int:
    count = 0

    for i in words:
        if i == s[:len(i)]:
            count += 1
    return count


if __name__ == '__main__':
    li_1 = ["a", "b", "c", "ab", "bc", "abc"]
    li_2 = ["ycwj", "hak", "v", "kjg", "zw", "vtes", "vom", "ii", "as", "v", "vo", "v", "w", "vomy", "loa", "fbm", "j",
            "v", "vo", "e", "y", "t", "eh", "yk", "bt", "x", "vomy", "vom", "yab", "v", "sydi", "wnb", "z", "v", "iygp",
            "vomy"]
    s_1 = "abc"
    s_2 = "vomy"
    print(count_prefixes(li_2, s_2))
