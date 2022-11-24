'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.
'''
class Solution:
    def secondHighest(self, s: str) -> int:
        flag = False
        for i in range(9, -1, -1):
            if str(i) in s:
                if flag:
                    return i
                else:
                    flag = True
        return -1
