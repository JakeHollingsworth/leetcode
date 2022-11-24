'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1, str2 = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        curr = ""
        for i in range(len(str1)):
            substr_len = i + 1
            if not len(str2) % substr_len and not len(str1) % substr_len:
                substr = str1[:i+1]
                if (substr * (len(str2) // substr_len)) == str2 and (substr * (len(str1)//substr_len) == str1 ):
                    curr = substr
        return curr
