'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        table = {}
        candidates = set(candidates)
        for n in range(2, target+1):
            if n in candidates:
                table[n] = [[n]]
            for m in table.copy():
                if n-m in table:
                    if n in table:
                        table[n] += [x + y for x in table[m] for y in table[n-m]]
                    else:
                        table[n] = [x + y for x in table[m] for y in table[n-m]]
            if n in table:
                # Drop duplicates
                table[n] = list(set(tuple(sorted(x)) for x in table[n]))
        return table[target] if target in table else []
