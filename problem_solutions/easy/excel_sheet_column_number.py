'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i, char in enumerate(columnTitle[::-1]):
            total += (ord(char)-64) * 26 ** i
        return total
