'''
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
'''
class Solution:
    def binaryGap(self, n: int) -> int:
        max_dist = 0
        dist = 0
        while n % 2 == 0:
            n //= 2
        while n > 0:
            if n % 2 != 0:
                max_dist = max(dist, max_dist)
                dist = 0
            dist += 1
            n //= 2
        return max_dist
