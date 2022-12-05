"""
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears
before every 'b' in the string. Otherwise, return false.
"""


def check(s: str) -> bool:
    if "ba" not in s:
        return True
    return False


if __name__ == '__main__':
    st = "aabaab"
    print(check(st))
