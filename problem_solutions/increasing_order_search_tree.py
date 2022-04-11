'''
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
'''
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def in_order_traversal(root):
            if not root:
                return []
            return in_order_traversal(root.left) + [root] + in_order_traversal(root.right)
        ordered_nodes = in_order_traversal(root)
        for i, n in enumerate(ordered_nodes):
            n.left = None
            n.right = ordered_nodes[i+1] if i + 1 < len(ordered_nodes) else None
        return ordered_nodes[0]
