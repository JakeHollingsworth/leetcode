'''
You are entering a competition, and are given two positive integers initialEnergy and initialExperience denoting your initial energy and initial experience respectively.

You are also given two 0-indexed integer arrays energy and experience, both of length n.

You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i] and experience[i] respectively. When you face an opponent, you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.

Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].

Before starting the competition, you can train for some number of hours. After each hour of training, you can either choose to increase your initial experience by one, or increase your initial energy by one.

Return the minimum number of training hours required to defeat all n opponents.
'''
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_needed = sum(energy) - initialEnergy + 1
        cumulative_exp_gained = [sum(experience[:i]) for i in range(len(experience) + 1)]
        exp_needed = max(experience[i] + 1 - (cumulative_exp_gained[i] + initialExperience) for i in range(len(experience)))
        return max(0, energy_needed) + max(0, exp_needed)
