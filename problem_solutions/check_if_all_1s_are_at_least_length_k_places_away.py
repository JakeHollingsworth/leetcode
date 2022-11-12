'''
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
'''
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        current = float('inf')
        for n in nums:
            if not n:
                current += 1
            else:
                if current < k:
                    return False
                current = 0
        return True
