'''
You are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.
'''
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        instructions = []
        m = 0
        while target:
            instructions += ["Push", "Pop"] * (target[0] - m - 1)
            m = target.pop(0)
            instructions.append("Push")
        return instructions 
