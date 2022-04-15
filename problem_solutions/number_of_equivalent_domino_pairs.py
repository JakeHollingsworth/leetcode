'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dom_dict = {}
        num_pairs = 0
        for d in dominoes:
            d = tuple(d)
            revd = (d[1],d[0])
            if d in dom_dict:
                num_pairs += dom_dict[d]
                dom_dict[d] += 1
            elif revd in dom_dict:
                num_pairs += dom_dict[revd]
                dom_dict[revd] += 1
            else:
                dom_dict[d] = 1
        return num_pairs
                
