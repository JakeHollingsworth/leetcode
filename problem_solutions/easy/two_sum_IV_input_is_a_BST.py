'''
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.
'''
class Solution:
    def inorder(self, root):
        left, right = [], []
        if not root:
            return None
        if root.left:
            left = self.inorder(root.left)
        if root.right:
            right = self.inorder(root.right)
        return left + [root.val] + right
            
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nodes = self.inorder(root)
        nodes = {n:i for i,n in enumerate(nodes)}
        for i, n in enumerate(nodes):
            if k-n in nodes and nodes[k - n] != i:
                return True
        return False
