'''
Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.

An integer m is a divisor of n if there exists an integer k such that n = k * m.
'''
class Solution:
    def isThree(self, n: int) -> bool:
        one_divisor = False
        for m in range(2, math.floor(math.sqrt(n) + 1)):
            if not n % m:
                if not m ** 2 == n:
                    return False
                else:
                    one_divisor = True
        return one_divisor
