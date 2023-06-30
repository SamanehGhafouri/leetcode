"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""
import collections


def can_construct(ransom_note: str, magazine: str) -> bool:
    ransom_note_dict = collections.Counter(ransom_note)
    magazine_dict = collections.Counter(magazine)

    count = 0
    for ch in ransom_note:
        if ch in magazine and magazine_dict[ch] >= ransom_note_dict[ch]:
            count += 1
    if count == len(ransom_note):
        return True
    return False


if __name__ == '__main__':
    ransom_note = "aab"
    magazine = "baaa"
    print(can_construct(ransom_note, magazine))
