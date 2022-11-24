'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x^y
        total = 0
        for i in range(32):
            total += (xor % 2)
            xor >>= 1
        return total
