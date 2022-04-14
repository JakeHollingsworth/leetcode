'''
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.
'''
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], val = 0) -> int:
        next_val = (val << 1) + root.val
        if not root.left and not root.right:
            return next_val
        elif not root.left:
            return self.sumRootToLeaf(root.right, next_val)
        elif not root.right:
            return self.sumRootToLeaf(root.left, next_val)
        else:
            return self.sumRootToLeaf(root.left, next_val) + self.sumRootToLeaf(root.right, next_val)
