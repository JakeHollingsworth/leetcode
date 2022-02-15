'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution:
    '''
    Canonical dynamical programming problem. Same solution as fibonacci. prev holds number of ways to reach previous step, prevprev holds
    the number of ways to reach step before prev.
    '''
    def climbStairs(self, n: int) -> int:
        if n < 3: return n
        prevprev, prev = 1, 2
        for i in range(2, n):
            prevprev, prev = prev, prev+prevprev
        return prev
