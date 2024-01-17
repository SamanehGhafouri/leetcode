"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters,
the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be
forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain
emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses
that actually receive mails.
"""
from typing import List


def unique_email_address(emails: List[str]) -> int:
    unique_emails = set()
    for email in emails:
        e = []
        at_indx = email.index('@')
        if '+' in email:
            p_indx = email.index('+')
            for ch in email[:p_indx]:
                if ch != ".":
                    e.append(ch)
        else:
            for ch in email[:at_indx]:
                if ch != ".":
                    e.append(ch)
        e.extend(email[at_indx:])
        unique_emails.add("".join(e))
    return len(unique_emails)


if __name__ == '__main__':
    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    print(unique_email_address(emails))