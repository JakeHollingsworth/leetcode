'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive_odds = 0
        for a in arr:
            if not a % 2:
                consecutive_odds = 0
            else:
                consecutive_odds += 1
            if consecutive_odds == 3:
                return True
        return False
