"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""


def hamming_distance(x: int, y: int) -> int:
    x_bit = bin(x)[2::]
    y_bit = bin(y)[2::]

    min_bits = min(len(x_bit), len(y_bit))
    max_bits = max(len(x_bit), len(y_bit))
    diff = max_bits - min_bits
    zeros = build_zeros(diff)

    if len(x_bit) < len(y_bit):
        x_bit = zeros + x_bit
    if len(x_bit) > len(y_bit):
        y_bit = zeros + y_bit

    h_distance = 0
    for i, j in zip(x_bit, y_bit):
        if i != j:
            h_distance += 1
    return h_distance


def build_zeros(diff: int):
    li = []
    for i in range(diff):
        li.append('0')
    return "".join(li)


if __name__ == '__main__':
    x = 1
    y = 4
    print(hamming_distance(x, y))
    print(build_zeros(2))
