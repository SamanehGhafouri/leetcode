"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


def reverse_words(s: str) -> str:
    words = []
    word = []
    for ch in s:
        if ch != " ":
            word.append(ch)
        else:
            if len(word) == 0:
                continue
            words.append("".join(word))
            word = []
    if len(word) != 0:
        words.append("".join(word))

    i = 0
    j = len(words) - 1

    while j > i:
        words[i], words[j] = words[j], words[i]
        i += 1
        j -= 1
    return " ".join(words)


if __name__ == '__main__':
    test_cases = [
        ("  hello world  ", "world hello"),
        ("the sky is blue", "blue is sky the"),
        ("a good   example", "example good a")
    ]
    for item in test_cases:
        print(item[1] == reverse_words(item[0]))
