"""
Given a string s and a character c that occurs in s, return an array of integers answer where
answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.
"""
from typing import List


def shortest_to_char(s: str, c: str) -> List[int]:
    set_c_indexes = set()

    for c_index in range(len(s)):
        if s[c_index] == c:
            set_c_indexes.add(c_index)
    if len(set_c_indexes) == 0:
        return []

    result = []
    helper_li = []
    for char in range(len(s)):
        for c_index in set_c_indexes:
            diff = abs(char - c_index)
            helper_li.append(diff)
        min_distance = min(helper_li)
        helper_li = []
        result.append(min_distance)
    return result


if __name__ == '__main__':
    string = "loveleetcode"
    ch = "e"
    print(shortest_to_char(string, ch))
