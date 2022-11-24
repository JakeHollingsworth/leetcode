'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution:
    '''
    We can read the roman numeral from left to right, adding the value of the symbol to a running sum. If the value of the symbol is 
    less than the previous 1, then we subtract from the total instead of add.
    '''
    def romanToInt(self, s: str) -> int:
        roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M': 1000}
        total = 0
        max_val = 1
        for char in s[::-1]:
            # First term handles sign of contribution
            if roman_map[char] >= max_val:
                total += roman_map[char]
            else:
                total -= roman_map[char]
            max_val = max(roman_map[char], max_val)
        return total
        
        
