'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s2 = sum([x**2 for x in nums])
        s = sum(nums)
        missing = ((n * (n+1) * (2*n + 1) / 6 - s2) / ((n * (n+1) / 2 ) - s) + n * (n+1)/2 - s)/2
        duplicated = ((n * (n+1) * (2*n + 1) / 6 - s2) / ((n * (n+1) / 2 ) - s) - n * (n+1)/2 + s)/2
        return [int(duplicated), int(missing)]
