'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
'''
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        for n in range(1, min(a,b) + 1):
            if not a % n and not b % n:
                count += 1
        return count
