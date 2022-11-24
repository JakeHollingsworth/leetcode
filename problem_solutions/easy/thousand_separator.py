'''
Given an integer n, add a dot (".") as the thousands separator and return it in string format.
'''
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_list = [c for c in str(n)][::-1]
        count = 0
        for i, k in enumerate(range(3, len(n_list), 3)):
            n_list.insert(k + i, '.')
        return "".join(n_list)[::-1]
