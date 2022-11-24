'''
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
'''
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parents = [None]
        level = [root]
        parent_x, parent_y = None, None
        while level:
            for i, (node, parent) in enumerate(zip(level, parents)):
                if node.val == x:
                    parent_x = parent
                elif node.val == y:
                    parent_y = parent
            if parent_x and parent_y:
                return parent_x != parent_y
            elif parent_x and not parent_y or parent_y and not parent_x:
                return False
            else:
                new_level = []
                new_parents = []
                for node in level:
                    children = []
                    if node.left:
                        children.append(node.left)
                        new_parents.append(node)
                    if node.right:
                        children.append(node.right)
                        new_parents.append(node)
                    new_level += children
                parents = new_parents
                level = new_level
        return False
