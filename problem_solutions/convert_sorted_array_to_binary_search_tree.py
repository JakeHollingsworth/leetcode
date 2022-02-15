'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode(nums[len(nums)//2])
        if len(nums) == 1:
            return root
        elif len(nums) == 2:
            root.left = self.sortedArrayToBST(nums[:len(nums)//2])
        else:
            root.left = self.sortedArrayToBST(nums[:len(nums)//2])
            root.right = self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root
