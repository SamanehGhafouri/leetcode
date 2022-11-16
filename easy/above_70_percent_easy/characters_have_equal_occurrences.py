"""
1941. Check if All Characters Have Equal Number of Occurrences
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number
of occurrences (i.e., the same frequency).
"""
import collections


def are_occurrences_equal(s: str) -> bool:
    return len(set(collections.Counter(s).values())) == 1


if __name__ == '__main__':
    string_s = "abacbc"
    print(are_occurrences_equal(string_s))
