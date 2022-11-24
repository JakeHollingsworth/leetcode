'''
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
'''
class Solution:
    def toHex(self, num: int) -> str:
        result = []
        if not num: return "0"
        sign = abs(num) / num
        num = abs(num)
        hexmap = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        while num > 0:
            result.append(num % 16)
            num //= 16
        if sign < 0:
            result = [15 - n for n in (result + (8-len(result)) * [0])]
            i = 0
            while i < len(result) and (result[i] + 1) == 16:
                result[i] = 0
                i += 1
            if i < len(result):
                result[i] += 1
            else:
                result.append(1)
        result = [hexmap[n] if n in hexmap else str(n) for n in result]
        return ("".join(result))[::-1]
        
