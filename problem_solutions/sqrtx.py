'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        # Newton Raphson
        def deriv(guess):
            return 4 * guess * (guess * guess - x)
        def error(guess):
            return (guess * guess - x) * (guess * guess - x)
        
        eps = 1e-3
        guess = x
        while abs(guess * guess - x) > eps:
            guess -= error(guess) / (deriv(guess) + eps)
        return int(guess)
