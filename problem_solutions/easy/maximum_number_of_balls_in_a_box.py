'''
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to the sum of digits of the ball's number. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.
'''
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def digit_sum(m):
            tot = 0
            while m > 0:
                tot += m % 10
                m //= 10
            return tot
        frequencies = {}
        for n in range(lowLimit, highLimit + 1):
            digit_tot = digit_sum(n)
            if digit_tot in frequencies:
                frequencies[digit_tot] += 1
            else:
                frequencies[digit_tot] = 1
        return max(frequencies.values())
