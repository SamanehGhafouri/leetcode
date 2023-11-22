"""
You are given a 0-indexed array of string words and two integers left and right.

A string is called a vowel string if it starts with a vowel character and ends with a vowel character where vowel
characters are 'a', 'e', 'i', 'o', and 'u'.

Return the number of vowel strings words[i] where i belongs to the inclusive range [left, right].
"""
from typing import List


def count_num_vowels(words: List[str], left: int, right: int) -> int:
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(left, right + 1):
        if words[i][0] in vowels and words[i][-1] in vowels:
            count += 1
    return count

if __name__ == '__main__':
    words = ["are", "amy", "u"]
    left = 0
    right = 2
    print(count_num_vowels(words, left, right))