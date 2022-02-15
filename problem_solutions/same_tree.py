'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p): return False
        if (not p and not q): return True
        if p.val == q.val:
            if p.left and q.left and p.right and q.right:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            elif p.left and q.left and not p.right and not q.right:
                return self.isSameTree(p.left, q.left)
            elif not p.left and not q.left and p.right and q.right:
                return self.isSameTree(p.right, q.right)
            elif not p.left and not q.left and not p.right and not q.right:
                return True
            else:
                return False       
        else:
            return False
