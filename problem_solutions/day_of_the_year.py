'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.
'''
class Solution:
    def dayOfYear(self, date: str) -> int:
        yr, mo, day = date.split('-')
        feb_days = 28 if int(yr) % 4 or (not int(yr) % 100 and int(yr) % 400) else 29
        days = [31,feb_days,31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cumulative = 0
        for i in range(int(mo) - 1):
            cumulative += days[i]
        return cumulative + int(day) 
