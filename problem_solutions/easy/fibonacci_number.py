'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
'''
class Solution:
    def fibmemo(self, n, memo):
        if n > 2:
            term1 = memo[n-1] if n-1 in memo else self.fibmemo(n-1, memo)
            term2 = memo[n-2] if n-2 in memo else self.fibmemo(n-2, memo)
            memo[n] = term1 + term2
        return memo[n]
        
    def fib(self, n: int) -> int:
        if not n:
            return 0
        return self.fibmemo(n,{1:1, 2:1})
