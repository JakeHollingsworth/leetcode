'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while stack and int(ch) < int(stack[-1]) and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
        if k > 0:
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"
