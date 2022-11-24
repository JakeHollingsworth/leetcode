'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr_set = set(arr)
        for n in arr_set:
            if 2 * n in arr_set and n != 0:
                return True
            elif n == 0:
                if sum([n == 0 for n in arr]) >= 2:
                    return True
        return False
