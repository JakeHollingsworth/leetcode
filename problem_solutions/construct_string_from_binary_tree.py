'''
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
'''
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        str_rep = ""
        if root and root.left and root.right:
            str_rep = f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
        elif root and root.left:
            str_rep = f"{root.val}({self.tree2str(root.left)})"
        elif root and root.right:
            str_rep = f"{root.val}()({self.tree2str(root.right)})"
        elif root:
            str_rep = str(root.val)
        return str_rep
