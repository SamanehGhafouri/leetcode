"""
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""

def str_str(haystack: str, needle: str) -> int:
    if needle not in haystack:
        return -1
    return haystack.index(needle)

def str_str_second_solution(haystack: str, needle: str) -> int:
    return haystack.find(needle)

def str_str_third_solution(haystack: str, needle: str) -> int:
    top = len(needle)
    for i in range(len(haystack)):
        if haystack[i:top + i] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    print(str_str_third_solution(haystack, needle))