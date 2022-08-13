"""
Given an array of strings words, return the first palindromic string in the array.
If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
"""
from typing import List


def first_palindrome(words: List[str]) -> str:
    first_pal_word = ""
    for word in words:
        if word[::-1] == word[:]:
            first_pal_word = word
            break
    if len(first_pal_word) == 0:
        return ""
    return first_pal_word


if __name__ == '__main__':
    arr_words = ["abc", "car", "ada", "racecar", "cool"]
    print(first_palindrome(arr_words))
