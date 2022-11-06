"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and
ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3
(inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
"""


def reverse_prefix(word: str, ch: str) -> str:
    ch_indexes = []
    for i in range(len(word)):
        if word[i] == ch:
            ch_indexes.append(i)
    char = min(ch_indexes)
    to_be_reversed = word[0:char+1]
    return to_be_reversed[::-1] + word[char+1:]


if __name__ == '__main__':
    w = "xyxzxe"
    c = "z"
    print(reverse_prefix(w, c))
