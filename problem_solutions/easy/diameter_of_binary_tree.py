'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
'''
class Solution:
    def get_diameter(self, root, diameter):
        if not root: return 0
        left_depth, right_depth, left_diameter, right_diameter = 0,0,0,0
        if root.left:
            left_depth, left_diameter = self.get_diameter(root.left, diameter)
        if root.right:
            right_depth, right_diameter = self.get_diameter(root.right, diameter)
        depth = max(left_depth, right_depth) + 1
        diameter = max(diameter, left_diameter, right_diameter, left_depth + right_depth)
        return depth, diameter
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.get_diameter(root, 0)
        return diameter
