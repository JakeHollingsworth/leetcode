'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.
'''
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        i = 0
        sub_table = {' ': ' '}
        for c in key:
            if c not in sub_table:
                sub_table[c] = alphabet[i]
                i += 1
        return ''.join(sub_table[c] for c in message)
