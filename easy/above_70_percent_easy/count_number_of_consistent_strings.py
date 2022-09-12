"""
You are given a string allowed consisting of distinct characters
and an array of strings words. A string is consistent if all
characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.
"""
from typing import List


def count_consistent_string(allowed: str, words: List[str]) -> int:
    count = 0
    set_allowed = set(allowed)

    for word in words:
        set_word = set(word)
        leftover = set_word - set_allowed
        if len(leftover) == 0:
            count += 1
    return count


if __name__ == '__main__':
    li_words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    allowed_ch = "cad"
    print(count_consistent_string(allowed_ch, li_words))
