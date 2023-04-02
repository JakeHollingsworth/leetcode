'''
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
'''
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        minimum_spell_strength = [success / x for x in potions]
        minimum_spell_strength.sort()

        def rightmost_binary_search(arr, target):
            l = 0
            r = len(arr)
            while l < r:
                m = (l+r)//2
                if arr[m] > target:
                    r = m
                else:
                    l = m+1
            return r
        
        pairs = [rightmost_binary_search(minimum_spell_strength, n) for n in spells]
        return pairs
