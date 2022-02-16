'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num:
            total += (num % 10)
            num //= 10
            if num == 0 and total > 9:
                num = total
                total = 0
        return total
