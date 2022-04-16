'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            d = n % 10
            product *= d
            total += d
            n //= 10
        return product - total
