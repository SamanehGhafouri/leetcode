"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
"""
from typing import List


def most_words_found(sentences: List[str]) -> int:
    number_of_words = []
    for sentence in sentences:
        number_of_words.append(len(sentence.split()))
    return max(number_of_words)


if __name__ == '__main__':
    sentences_li = ["please wait", "continue to fight", "continue to win"]
    print(most_words_found(sentences_li))
