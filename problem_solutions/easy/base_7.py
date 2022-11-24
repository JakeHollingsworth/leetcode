'''
Given an integer num, return a string of its base 7 representation.
'''
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num: return str(num)
        result = ""
        sign = num / abs(num)
        num = abs(num)
        while num > 0:
            result += str(num % 7)
            num //=7
        return ('-' if sign < 0 else '') + result[::-1]
