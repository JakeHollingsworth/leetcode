'''
A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
'''
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode], val = None) -> bool:
        if val is None:
            val = root.val
        if not root:
            return True
        elif val != root.val:
            return False
        else:
            return self.isUnivalTree(root.left, val) and self.isUnivalTree(root.right, val)
