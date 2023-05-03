"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


def roman_to_int(s: str) -> int:
    roman_symbol_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = s[::-1]
    stack = [s[0]]
    total_sum = roman_symbol_values[s[0]]
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            total_sum += roman_symbol_values[s[i]]
        else:
            stack.append(s[i])
            val = roman_symbol_values[s[i]]
            if val > total_sum:
                total_sum += val
            else:
                total_sum -= val
    return total_sum


if __name__ == '__main__':
    roman = "MCMXCIV"
    print(roman_to_int(roman))
