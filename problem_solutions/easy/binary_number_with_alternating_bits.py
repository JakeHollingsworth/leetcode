'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        while n:
            if not (n ^ (n >> 1)) % 2:
                return False
            n >>= 1
        return True    
