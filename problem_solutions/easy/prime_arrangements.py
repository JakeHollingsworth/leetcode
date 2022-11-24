'''
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.
'''
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def fact(n, memo={}):
            if n in memo:
                return memo[n]
            if n == 0 or n == 1:
                memo[n] = 1
            else:
                memo[n] = n * fact(n-1, memo)
            return memo[n]
            
        # Get all primes
        n_primes = 0
        for m in range(2, n+1):
            prime = 1
            for a in range(2, int(sqrt(m)) + 1):
                if not m % a:
                    prime = 0
            n_primes += prime
        return (fact(n_primes) * fact(n - n_primes)) % (10**9 + 7)
