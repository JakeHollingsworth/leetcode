'''
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
'''
class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = []
        while num > 0:
            digits.append(num % 10)
            num //= 10
        swap = True
        result = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 6 and swap:
                digits[i] = 9
                swap = False
            result *= 10
            result += digits[i]
        return result
