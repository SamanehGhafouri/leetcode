"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence
is a pangram, or false otherwise.
"""


def check_if_pangram(sentence: str) -> bool:
    set_sentence = set(sentence)
    if len(set_sentence) == 26:
        return True
    return False


if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(check_if_pangram(sentence))
