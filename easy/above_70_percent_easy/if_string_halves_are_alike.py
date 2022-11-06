"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a
be the first half and b be the second half.

Two strings are alike if they have the same number of vowels
('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


def halves_are_alike(s: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    len_s = len(s)
    half_index = len_s // 2
    a = s[:half_index]
    b = s[half_index:]

    count_v_in_a = 0
    count_v_in_b = 0
    for ch in a:
        if ch in vowels:
            count_v_in_a += 1
    for ch in b:
        if ch in vowels:
            count_v_in_b += 1
    return count_v_in_a == count_v_in_b


if __name__ == '__main__':
    string = "book"
    print(halves_are_alike(string))
