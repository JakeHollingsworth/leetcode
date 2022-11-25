'''
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.
'''
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(digits)
        ends = [d for d in freq.keys() if not d % 2]
        starts = [d for d in freq.keys() if d]
        res = []
        for s in starts:
            for e in ends:
                start_end_flag = (s == e)
                for m in freq.keys():
                    digit = 100 * s + 10 * m + e
                    if m == s or m == e:
                        if freq[m] >= (3 if start_end_flag else 2):
                            res.append(digit)
                    elif not start_end_flag or freq[s] >= 2:
                        res.append(digit)
        return sorted(res)
