'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans= 0
        ans_odd = set([])
        for i in range(0, 34, 2):
            ans += 2 ** i
            ans_odd.add(ans)
        ans_even = {ans >> 1 for ans in ans_odd}
        return (n in ans_odd  or n in ans_even)       
