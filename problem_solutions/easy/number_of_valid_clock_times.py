'''
You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 to 9.
'''
class Solution:
    def countTime(self, time: str) -> int:
        hours = time[:2]
        if hours == '??':
            h = 24
        elif hours.count('?') == 0:
            h = 1
        elif hours[1] == '?':
            h = 10 if hours[0] in '01' else 4
        else:
            h = 3 if hours[1] in '0123' else 2 
        m1 = 6 if time[3] == '?' else 1
        m2 = 10 if time[4] == '?' else 1
        return h * m1 * m2
