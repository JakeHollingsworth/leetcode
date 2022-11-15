'''
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
'''
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        f_left = 0
        f_right = max(right for right in range(len(colors)) if colors[right] != colors[f_left])
        r_right = len(colors) - 1
        r_left = min(left for left in range(len(colors)) if colors[left] != colors[r_right])
        return max(f_right - f_left, r_right - r_left)
