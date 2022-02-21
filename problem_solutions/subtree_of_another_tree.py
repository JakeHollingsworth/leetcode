'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''
class Solution:
    def tree_equality(self, root1, root2):
        if not root1 and not root2: 
            return True
        elif (root1 and not root2) or (not root1 and root2): 
            return False
        if root1.val == root2.val and \
           self.tree_equality(root1.left, root2.left) and \
           self.tree_equality(root1.right, root2.right):
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack[0]
            if self.tree_equality(node, subRoot):
                return True
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                stack.pop(0)
        return False
            
