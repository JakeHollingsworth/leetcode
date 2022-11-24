'''
You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year. The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.
'''
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pop = 0
        max_pop = 0
        max_yr = min([min(yr) for yr in logs])
        ordered_yrs = []
        for birth_yr, death_yr in logs:
            ordered_yrs.append((birth_yr, 1))
            ordered_yrs.append((death_yr, -1))
        ordered_yrs.sort()
        for yr, delta in ordered_yrs:
            pop += delta
            if pop > max_pop:
                max_pop = pop
                max_yr = yr
        return max_yr
