'''
Reverse bits of a given 32 bits unsigned integer.
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = result << 1
            result += n % 2
            n = n >> 1
        return result
