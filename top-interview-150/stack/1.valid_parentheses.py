"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    data = {'(': ')', '[': ']', '{': '}'}
    stack = [s[0]]
    for p in range(1, len(s)):
        if len(stack) != 0:
            if stack[-1] in data and s[p] == data[stack[-1]]:
                stack.pop()
            else:
                stack.append(s[p])
        else:
            stack.append(s[p])
    return len(stack) == 0


if __name__ == '__main__':
    s = "){"  # False
    # s = "()[]{}" # True
    # s = "([)]" # False
    print(is_valid(s))
