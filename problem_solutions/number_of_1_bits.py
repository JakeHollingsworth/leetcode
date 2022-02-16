'''
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        for i in range(32):
            num_ones += n % 2
            n = n >> 1
        return num_ones
