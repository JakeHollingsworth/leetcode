'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = (num1, num2) if len(num1) < len(num2) else (num2, num1)
        carry = 0
        result = []
        for d1, d2 in zip(num1[::-1] + "0" * (len(num2) - len(num1)), num2[::-1]):
            d3 = (int(d1) + int(d2) + carry)
            result.append(str(d3 % 10))
            carry = d3 // 10
        if carry:
            result.append(str(carry))
        return "".join(result)[::-1]
