'''
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.
'''
from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = [int(x) for x in date1.split('-')]
        d2 = [int(x) for x in date2.split('-')]
        d1, d2 = date(*d1), date(*d2)
        return abs((d2 - d1).days)
        
