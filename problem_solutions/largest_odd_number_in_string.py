'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i, c in enumerate(num[::-1]):
            if int(c) % 2:
                return num[:len(num) - i]
        return ''
