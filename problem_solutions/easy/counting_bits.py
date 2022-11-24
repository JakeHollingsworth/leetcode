'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        return [format(i, 'b').count("1") for i in range(n+1)]
