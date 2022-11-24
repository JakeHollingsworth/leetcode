'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
'''
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], history = "") -> List[str]:
        if not history:
            history = str(root.val)
        else:
            history += f"->{root.val}"
        if not root.left and not root.right:
            return [history]
        if not root.left:
            return self.binaryTreePaths(root.right, history=history)
        if not root.right:
            return self.binaryTreePaths(root.left, history=history)
        return self.binaryTreePaths(root.left, history=history) + \
               self.binaryTreePaths(root.right, history=history)
