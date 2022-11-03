"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""


def maximum_69_number(num: int) -> int:
    num_to_str = str(num)
    numbers = []
    for n in num_to_str:
        numbers.append(n)

    for i in range(len(numbers)):
        if numbers[i] == "6":
            numbers[i] = "9"
            break
    return int("".join(numbers))


if __name__ == '__main__':
    n = 9996
    print(maximum_69_number(n))
