"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""


def word_pattern(pattern: str, s: str) -> bool:
    if len(pattern) != len(s.split()):
        return False
    dict_result = {}
    false_counter = 0
    for i, j in zip(pattern, s.split()):
        if i not in dict_result and j not in dict_result.values():
            dict_result[i] = j
        elif i not in dict_result and j in dict_result.values():
            false_counter += 1
        elif i in dict_result and j != dict_result[i]:
            false_counter += 1
    if false_counter != 0:
        return False
    return True


if __name__ == '__main__':
    pattern = "aaaa"  # return False
    s = "dog cat cat dog"
    # pattern = "abba" # return False
    # s = "dog cat cat fish"
    # pattern = "abba" # return True
    # s = "dog cat cat dog"

    print(word_pattern(pattern, s))
