"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:

    # find palindrome by converting the string to an integer
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        reverse_string = string_x[::-1]
        return string_x == reverse_string

    # find palindrome without converting x to string
    def isPalindrome2(self, x: int) -> bool:
        n, y = x, 0
        f = lambda: (y * 10) + n % 10
        while n > 0:
            n, y = n // 10, f()
        return y == x


if __name__ == '__main__':
    num = Solution()
    print(num.isPalindrome(12100121))
    print(num.isPalindrome2(1214))
