'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (1 if (low % 2) or (high % 2) else 0)
