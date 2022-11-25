'''
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to the character 'a'.


Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.
'''
class Solution:
    def minTimeToType(self, word: str) -> int:
        def mod_dist(c1, c2):
            return min(abs(ord(c2) - ord(c1)), abs(ord(c2) - 26 - ord(c1)), abs(ord(c2) + 26 - ord(c1)))
        total_time = mod_dist('a', word[0])
        for i in range(len(word) - 1):
            total_time += mod_dist(word[i], word[i+1])
        return total_time + len(word)
