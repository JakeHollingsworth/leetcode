'''
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.
'''
class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for x in range(1, n+1):
            for y in range(x+1, n+1): # x=y ingnored since this will always have a factor of sqrt(2) on hypotenuse
                if math.sqrt(x**2 + y**2) == int(math.sqrt(x**2 + y**2)) and math.sqrt(x**2 + y**2) <= n:
                    count += 2
        return count
