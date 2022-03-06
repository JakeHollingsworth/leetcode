'''
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            mid = left + (right - left) // 2
            if target == letters[mid]:
                left = mid
                right = mid
            elif target < letters[mid]:
                right = mid
            else:
                left = mid + 1
        letters += letters[0]
        while letters[right] == target:
            right += 1
        return letters[right]
