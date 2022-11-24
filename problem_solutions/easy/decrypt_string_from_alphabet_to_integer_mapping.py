'''
You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.
'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        nums_to_map = []
        i = 0
        while i < len(s):
            c = s[i]
            if '#' not in s[i:i+3]:
                nums_to_map.append(c)
                i += 1
            else:
                nums_to_map.append(s[i:i+2])
                i += 3
        return "".join([chr(int(num) + 96) for num in nums_to_map])
