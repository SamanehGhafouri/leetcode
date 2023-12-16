"""
Given an array of strings words and a character separator, split each string in words by separator.

Return an array of strings containing the new strings formed after the splits, excluding empty strings.

Notes

separator is used to determine where the split should occur, but it is not included as part of the resulting strings.
A split may result in more than two strings.
The resulting strings must maintain the same order as they were initially given.
"""
from typing import List


def split_words_by_separator(words: List[str], separator: str) -> List[str]:
    result = []
    for word in words:
        if separator in word:
            result.extend(word.split(separator))
        else:
            result.append(word)
    return list(filter(None,result))


if __name__ == '__main__':
    words = ["one.two.three","four.five","six"]
    separator = "."
    print(split_words_by_separator(words, separator))
