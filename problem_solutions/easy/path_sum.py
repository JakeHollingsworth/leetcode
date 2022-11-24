'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        else:
            opt1, opt2 = False, False
            if root.left:
                opt1 = self.hasPathSum(root.left, targetSum - root.val)
            if root.right:
                opt2 = self.hasPathSum(root.right, targetSum - root.val)
            return opt1 or opt2

