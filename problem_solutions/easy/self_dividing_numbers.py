'''
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.

Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].
'''
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for n in range(left, right+1):
            digits = []
            m = n
            while n > 0:
                digits.append(n % 10)
                n //= 10
            if all([d != 0 and not m % d for d in digits]):
                ret.append(m)
        return ret
