'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        k = -1
        n_var = n
        while n_var > 1:
            ans.append(k)
            k = -k if k < 0 else -k-1
            n_var -= 1
        ans.append(0 if n % 2 else k)
        return ans
