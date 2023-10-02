"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character
is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
"""
import collections


def frequency_sort(s: str) -> str:
    sorted_dict = sorted(collections.Counter(s).items(), key=lambda item: item[1])
    result = []
    while sorted_dict:
        key, val = sorted_dict.pop()
        for _ in range(val):
            result.append(key)
    return "".join(result)


if __name__ == '__main__':
    st = "Aabb"
    # st = "tree"
    print(frequency_sort(st))