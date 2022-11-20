"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end
of the merged string.

Return the merged string.
"""


def merge_alternately(word1: str, word2: str) -> str:
    min_len = min(len(word1), len(word2))
    if len(word1) == min_len:
        max_len_word = word2
    else:
        max_len_word = word1
    li = []
    for i, j in zip(word1, word2):
        li.append(i)
        li.append(j)
    return "".join(li) + max_len_word[min_len::]


if __name__ == '__main__':
    word1 = "ab"
    word2 = "pqrs"
    print(merge_alternately(word1, word2))
