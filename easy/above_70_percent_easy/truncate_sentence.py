"""
A sentence is a list of words that are separated by
a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s and an integer k. You want to truncate s such that it
contains only the first k words. Return s after truncating it.
"""


def truncate_sentence(s: str, k: int) -> str:

    return " ".join(s.split()[:k])


if __name__ == '__main__':

    sentence = "Hello how are you Contestant"
    k_num = 4
    print(truncate_sentence(sentence, k_num))