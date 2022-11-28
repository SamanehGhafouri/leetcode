"""
The numerical value of some string of lowercase English letters s is the concatenation of the letter values
of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it,
we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English
letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of
targetWord, or false otherwise.
"""


def is_sum_equal(firstWord: str, secondWord: str, targetWord: str) -> bool:
    letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    f_numerical = ""
    for ch in firstWord:
        if ch in letters:
            f_numerical += str(letters[ch])

    s_numerical = ""
    for ch in secondWord:
        if ch in letters:
            s_numerical += str(letters[ch])

    t_numerical = ""
    for ch in targetWord:
        if ch in letters:
            t_numerical += str(letters[ch])

    return int(f_numerical) + int(s_numerical) == int(t_numerical)


if __name__ == '__main__':
    f = "j"
    s = "j"
    t = "bi"
    print(is_sum_equal(f, s, t))
