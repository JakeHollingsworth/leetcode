'''
You are given a string number representing a positive integer and a character digit.

Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.
'''
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = []
        for i, c in enumerate(number):
            if c == digit:
                res.append(number[:i] + (number[i+1:] if i + 1 < len(number) else ''))
        max_val = max(int(s) for s in res)
        for s in res:
            if int(s) == max_val:
                return s 
        return number
