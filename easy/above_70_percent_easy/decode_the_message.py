"""
Decode the Message
You are given the strings key and message, which represent a cipher key and a secret message, respectively.
The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet),
we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
"""


def decode_message(key: str, message: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mapping = {' ': ' '}
    i = 0
    res = ''

    for ch in key:
        if ch not in mapping:
            mapping[ch] = alphabet[i]
            i += 1

    for ch in message:
        res += mapping[ch]
    return res


if __name__ == '__main__':
    key = "the quick brown fox jumps over the lazy dog"
    mesg = "vkbs bs t suepuv"
    print(decode_message(key, mesg))
