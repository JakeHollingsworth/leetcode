'''
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
'''
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2,3,5,7,11,13,17,19,23,29,31])
        total = 0
        for n in range(left, right+1):
            set_bits = 0
            while n > 0:
                set_bits += (n % 2)
                n >>= 1
            if set_bits in primes:
                total += 1
        return total
