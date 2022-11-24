'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [cost[-1], cost[-2]]
        for i, c in enumerate(cost[::-1][2:]):
            min_cost.append(c + min(min_cost[i], min_cost[i+1]))
        return min(min_cost[-1], min_cost[-2])
