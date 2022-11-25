'''
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
'''
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def get_bits(n):
            bits = 0
            while n > 0:
                bits += 1 if n % 2 else 0
                n //= 2
            return bits
        sort_arr = sorted([(get_bits(n), n) for n in arr])
        return [n for _, n in sort_arr]
