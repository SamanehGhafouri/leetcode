"""
You are given a 0-indexed array words consisting of distinct strings.

The string words[i] can be paired with the string words[j] if:

The string words[i] is equal to the reversed string of words[j].
0 <= i < j < words.length.
Return the maximum number of pairs that can be formed from the array words.

Note that each string can belong in at most one pair.
"""
from typing import List


def max_number_of_string_pairs(words: List[str]) -> int:
    set_words = set(words)
    seen = set()
    count = 0
    for w in words:
        if w[::-1] in set_words and w[::-1] not in seen:
            if w[0] != w[1]:
                count += 1
                seen.add(w)
    return count


if __name__ == '__main__':
    words = ["cd", "ac", "dc", "ca", "zz"]
    print(max_number_of_string_pairs(words))
