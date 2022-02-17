'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 0
        while n ** 2 < num:
            n+=1
        return n ** 2 == num
