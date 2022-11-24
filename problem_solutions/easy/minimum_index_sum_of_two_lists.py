'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
'''
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {s:i for i,s in enumerate(list1)}
        dict2 = {s:i for i,s in enumerate(list2)}
        min_index_sum = float('inf')
        ans = []
        for s, i in dict1.items():
            if s in dict2:
                if dict2[s] + i == min_index_sum:
                    ans.append(s)
                elif dict2[s] + i < min_index_sum:
                    min_index_sum = dict2[s] + i
                    ans = [s]
        return ans
