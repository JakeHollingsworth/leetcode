'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        townees = {i+1: {'trusts': 0, 'trusted':0} for i in range(n)}
        for giver, target in trust:
            if giver != target:
                townees[giver]['trusts'] += 1
                townees[target]['trusted'] += 1
        judge = -1
        for townee, edges in townees.items():
            if edges['trusts'] == 0 and edges['trusted'] == n - 1:
                if judge != -1:
                    return -1
                else:
                    judge = townee
        return judge
