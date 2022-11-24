'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            i = 1
            while i <= len(digits) and digits[-i] == 9:
                i+=1
            if i-1 == len(digits):
                return [1] + [0 for _ in digits]
            else:
                digits[-i] += 1
                for j in range(1, i):
                    digits[-j] = 0
        else:
            digits[-1] += 1
        return digits
