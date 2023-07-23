"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
"""


def is_isomorphic(s: str, t: str) -> bool:
    map_s = []
    map_t = []
    s_dict = {}
    t_dict = {}
    if len(s) != len(t):
        return False
    for ch_s, ch_t in zip(s, t):
        if ch_s not in s_dict:
            s_dict[ch_s] = len(s_dict) + 1
        if ch_t not in t_dict:
            t_dict[ch_t] = len(t_dict) + 1
        map_s.append(s_dict[ch_s])
        map_t.append(t_dict[ch_t])
    return map_s == map_t


def is_isomorphic_faster(s: str, t: str) -> bool:
    len_zip = len(set(zip(s, t)))
    return len_zip == len(set(s)) == len(set(t))


if __name__ == '__main__':
    test_cases = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("bbbaaaba", "aaabbbba", False),
        ("bba", "bba", True),
        ("bba", "adc", False)
    ]
    for test_case in test_cases:
        expected = test_case[2]
        actual = is_isomorphic_faster(test_case[0], test_case[1])
        print(expected == actual)
