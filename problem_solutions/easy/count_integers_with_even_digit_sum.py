'''
Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

The digit sum of a positive integer is the sum of all its digits.
'''
class Solution:
    def countEven(self, num: int) -> int:
        num_copy = num
        digits = []
        while num_copy:
            digits.append(num_copy % 10)
            num_copy //= 10
        return (num - (sum(digits) % 2)) // 2 
