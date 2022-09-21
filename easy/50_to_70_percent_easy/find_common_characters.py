"""
Given a string array words, return an array of all characters that show up in all
strings within the words (including duplicates). You may return the answer in any order.
"""

from typing import List


def common_chars(words: List[str]) -> List[str]:
    common_chs = set(words[0])
    for i in range(1, len(words)):
        common_chs = set(words[i]).intersection(common_chs)

    dict_count = {}
    for word in words:
        mini_dict = {}
        for ch in word:
            if ch not in common_chs:
                continue
            if ch in mini_dict:
                mini_dict[ch] += 1
            else:
                mini_dict[ch] = 1

        for ch, cnt in mini_dict.items():
            if ch in dict_count:
                dict_count[ch].add(cnt)
            else:
                dict_count[ch] = {cnt}

    result = []
    for char, set_cnts in dict_count.items():
        for _ in range(min(set_cnts)):
            result.append(char)
    return result


if __name__ == '__main__':
    wds = ["bcaddcdd", "cbcdccdd", "ddccbdda", "dacbbdad", "dababdcb", "bccbdaad", "dbccbabd", "accdddda"]
    print(common_chars(wds))
