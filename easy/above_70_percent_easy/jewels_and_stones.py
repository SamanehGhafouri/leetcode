"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""


def num_jewels_in_stones(jewels: str, stones: str) -> int:
    count = 0
    for ch in stones:
        if ch in jewels:
            count += 1
    return count


if __name__ == '__main__':
    j = "aA"
    s = "ZZanQA"
    print(num_jewels_in_stones(j, s))
