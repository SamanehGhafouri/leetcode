"""
You are given a string s of lowercase English letters and an array widths denoting how many pixels wide each
lowercase English letter is. Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels. Starting at the
beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels.
Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this
process until you have written all of s.

Return an array result of length 2 where:

result[0] is the total number of lines.
result[1] is the width of the last line in pixels.
"""
from typing import List


def num_of_lines(widths: List[int], s: str) -> List[int]:
    characters = []
    line_counter = 0
    count = 0
    for ch in s:
        characters.append(ch)
        count += widths[ord(ch) - ord('a')]
        if count > 100:
            count = 0
            count += widths[ord(characters.pop()) - ord('a')]
            line_counter += 1
    return [line_counter + 1, count]


if __name__ == '__main__':
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"
    print(num_of_lines(widths, s))
