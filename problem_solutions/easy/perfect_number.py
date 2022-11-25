'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        dummy = num
        prime_factors = []
        div = 2
        while dummy > 1 and (prime_factors or div < math.sqrt(num)):
            while not dummy % div:
                prime_factors.append(div)
                dummy //= div
            div += 1
        divisors = set([])
        for r in range(1, len(prime_factors)):
            all_factors = itertools.combinations(prime_factors, r)
            for f in all_factors:
                divisors.add(prod(f))
        return sum(list(divisors)) + 1 == num and num != 1
