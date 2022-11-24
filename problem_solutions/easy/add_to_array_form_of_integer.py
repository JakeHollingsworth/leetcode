'''
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
'''
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def from_array_form(arr):
            num = arr.pop(0)
            while arr:
                num *= 10
                num += arr.pop(0)
            return num
        def to_array_form(n):
            arr = []
            while n:
                arr.append(n % 10)
                n //= 10
            return arr[::-1]
        n = from_array_form(num)
        n += k
        return to_array_form(n)
