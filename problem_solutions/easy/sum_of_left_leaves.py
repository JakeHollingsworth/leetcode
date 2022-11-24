'''
Given the root of a binary tree, return the sum of all left leaves.
'''
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], add=False) -> int:
        total = root.val if add and not (root.left or root.right) else 0
        if root.left:
            total += self.sumOfLeftLeaves(root.left, True)
        if root.right:
            total += self.sumOfLeftLeaves(root.right, False)
        return total
