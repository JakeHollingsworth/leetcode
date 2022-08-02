'''
Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's
'''
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones_seg_flag = s[0] == '1'
        streak = 0
        max_ones_streak = 0
        max_zeros_streak = 0
        for c in s:
            if ones_seg_flag:
                if c == '1':
                    streak += 1
                    max_ones_streak = max(streak, max_ones_streak)
                else:
                    streak = 1
                    ones_seg_flag = False
                    max_zeros_streak = max(streak, max_zeros_streak)
            else:
                if c == '0':
                    streak += 1
                    max_zeros_streak = max(streak, max_zeros_streak)
                else:
                    streak = 1
                    ones_seg_flag = True
                    max_ones_streak = max(streak, max_ones_streak)
        return max_ones_streak > max_zeros_streak
