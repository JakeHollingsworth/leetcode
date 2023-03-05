'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
'''

class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = 1 if x > 0 else -1
        MAX_INT = 2 ** 31 - (1 if sign > 0 else 0)
        x = abs(x)
        while x:
            digit = x % 10
            if ((MAX_INT - digit) / 10) < ans:
                return 0
            else:
                ans = 10 * ans + digit
            x //= 10
        return sign * ans
