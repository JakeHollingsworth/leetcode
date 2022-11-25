'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            title = chr(65 + (columnNumber-1) % 26) + title
            columnNumber = (columnNumber-1) // 26
        return title
