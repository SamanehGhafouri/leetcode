"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented
as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple
valid permutations perm, return any of them.
"""
from typing import List


def di_string_match(s: str) -> List[int]:
    nums = list(range(len(s) + 1))
    out = []
    for i in range(len(s)):
        if s[i] == 'I':
            out.append(nums.pop(0))
        else:
            out.append(nums.pop())

    out.append(nums.pop())
    return out


if __name__ == '__main__':
    word_string = "DIDI"
    print(di_string_match(word_string))