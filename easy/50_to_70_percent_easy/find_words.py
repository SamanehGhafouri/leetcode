"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

from typing import List
from collections import Counter


def find_words(words: List[str], chars: str) -> int:
    sum_len_strings = 0
    for word in words:
        if Counter(word) <= Counter(chars):
            sum_len_strings += len(word)
    return sum_len_strings


if __name__ == '__main__':
    w = ["cat", "bt", "hat", "tree"]
    c = "atach"
    print(find_words(w, c))
