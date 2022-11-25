'''
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
'''
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '1' * s.count('1') in s
