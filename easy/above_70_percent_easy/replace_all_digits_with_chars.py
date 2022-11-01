"""
You are given a 0-indexed string s that has lowercase English letters in its even indices and digits in its odd indices.

There is a function shift(c, x), where c is a character and x is a digit, that returns the xth character after c.

For example, shift('a', 5) = 'f' and shift('x', 0) = 'x'.
For every odd index i, you want to replace the digit s[i] with shift(s[i-1], s[i]).

Return s after replacing all digits. It is guaranteed that shift(s[i-1], s[i]) will never exceed 'z'.
"""
import string


def replace_digits(s: str) -> str:
    alphabets = list(string.ascii_lowercase)
    new_string = []

    for i in range(0, len(s) - 1, 2):
        new_string.append(s[i])
        index_alphabet_to_replace = alphabets.index(s[i]) + int(s[i + 1])
        new_string.append(alphabets[index_alphabet_to_replace])
    if len(s) % 2 == 0:
        return "".join(new_string)
    elif len(s) % 2 != 0 and s[-1].isdigit() is False:
        return "".join(new_string) + s[-1]


if __name__ == '__main__':
    st = "a1b2c3d4e"
    print(replace_digits(st))
    print(replace_digits(st) == "abbdcfdhe")
