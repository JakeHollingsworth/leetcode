'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
'''
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = {}
        for w in arr:
            if w in count_dict:
                count_dict[w] += 1
            else:
                count_dict[w] = 1
        curr_k = 0
        for w in arr:
            if count_dict[w] == 1:
                curr_k += 1
                if curr_k == k:
                    return w
        return ""
