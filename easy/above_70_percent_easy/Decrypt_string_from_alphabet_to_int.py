"""
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
"""


def freq_alphabets(s: str) -> str:
    alphabet_map = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
                    '10': 'j', '11': 'k', '12': 'l', '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q',
                    '18': 'r', '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w', '24': 'x', '25': 'y', '26': 'z'}

    new_s = []
    i = len(s) - 1
    while i >= 0:
        ch = s[i]
        if ch == "#":
            key = s[i-2:i]
            new_s.append(alphabet_map[key])
            i -= 3
        else:
            new_s.append(alphabet_map[ch])
            i -= 1
    return "".join(new_s[::-1])


if __name__ == '__main__':
    st = "10#11#12"
    print(freq_alphabets(st))
