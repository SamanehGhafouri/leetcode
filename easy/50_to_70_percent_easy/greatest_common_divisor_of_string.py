"""
For two strings s and t, we say "t divides s" if and only if
s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
import math


def gcd_div(str1, str2):
    if len(str1) < len(str2):
        min_str = str1
    else:
        min_str = str2

    len_gcd = math.gcd(len(str1), len(str2))
    gcd_str = min_str[:len_gcd]

    # total count of the gcd_str in each string
    total_count = str1.count(gcd_str) + str2.count(gcd_str)
    # total division of length of each string by length of gcd
    total_q = len(str1) // len_gcd + len(str2) // len_gcd

    if total_count == total_q:
        return gcd_str
    return ""


if __name__ == '__main__':
    str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    print(gcd_div(str1, str2))
