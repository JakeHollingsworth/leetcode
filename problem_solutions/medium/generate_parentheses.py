'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        start = [('', 0, 0)]
        ans = []
        for i in range(2 * n):
            for x, opn, closed in start:
                if opn < n:
                    ans.append((x + '(', opn + 1, closed))
                if closed < opn:
                    ans.append((x + ')', opn, closed + 1))
            start = ans.copy()
            ans = []
        return [tup[0] for tup in start]
