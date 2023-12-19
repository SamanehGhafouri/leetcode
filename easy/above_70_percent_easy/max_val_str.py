"""
The value of an alphanumeric string can be defined as:

The numeric representation of the string in base 10, if it comprises of digits only.
The length of the string, otherwise.
Given an array strs of alphanumeric strings, return the maximum value of any string in strs.
"""
from typing import List


def maximum_value(strs: List[str]) -> int:
    max_len = 0
    for st in strs:
        if st.isdigit():
            if int(st) > max_len:
                max_len = int(st)
        elif st.isalpha():
            if len(st) > max_len:
                max_len = len(st)
        else:
            if len(st) > max_len:
                max_len = len(st)
    return max_len



if __name__ == '__main__':
    strs = ["1","01","001","0001"]
    print(maximum_value(strs))