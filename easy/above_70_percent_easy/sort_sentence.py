"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.
"""


def sort_sentence(s: str) -> str:
    li_words = s.split()
    new_li = sorted(li_words, key=lambda x: x[-1])
    result = []
    for word in new_li:
        result.append(word[:-1])
    return " ".join(result)


if __name__ == '__main__':
    sentence = "is2 sentence4 This1 a3"
    print(sort_sentence(sentence))
