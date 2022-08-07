"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
"-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call
such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.
"""

from typing import List


def unique_morse_representations(words: List[str]) -> int:
    """All the morse code for 26 english letters"""
    all_letters_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                        "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--",
                        "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-",
                        "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
    morse_words = []
    morse_word = []

    number_of_transformation = {}

    for word in words:
        for letter in word:
            if letter in all_letters_code:
                morse_word.append(all_letters_code[letter])
        morse_words.append("".join(morse_word))
        morse_word.clear()

    for morse_word in morse_words:
        if morse_word not in number_of_transformation:
            number_of_transformation[morse_word] = 1
        else:
            number_of_transformation[morse_word] += 1

    return len(number_of_transformation)


if __name__ == '__main__':
    li_words = ["gin", "zen", "gig", "msg"]
    print(unique_morse_representations(li_words))
