"""
Given a string s, reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
"""


def reverse_words(s: str) -> str:
    li_words = s.split()
    li_reverse = []
    for word in li_words:
        li_reverse.append(word[::-1])
    return " ".join(li_reverse)


if __name__ == '__main__':
    st = "Let's take LeetCode contest"
    print(reverse_words(st))
