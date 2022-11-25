'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = 'balloon'
        counts = {}
        for c in text:
            counts[c] = counts[c] + 1 if c in counts else 1
        contained = True
        num_repeats = 0
        while contained:
            for c in target:
                if c not in counts or not counts[c]:
                    contained = False
                else:
                    counts[c] -= 1
            num_repeats += 1 if contained else 0
        return num_repeats
            
