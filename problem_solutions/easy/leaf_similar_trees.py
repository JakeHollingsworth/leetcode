'''
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_sequence(root):
            nodes = [root]
            while any([n.left or n.right for n in nodes]):
                new_nodes = []
                for n in nodes:
                    if n.left:
                        new_nodes.append(n.left)
                    if n.right:
                        new_nodes.append(n.right)
                    if not n.left and not n.right:
                        new_nodes.append(n)
                nodes = new_nodes
            return nodes
        root1_sequence = leaf_sequence(root1)
        root2_sequence = leaf_sequence(root2)
        for n1, n2 in zip(root1_sequence, root2_sequence):
            if n1.val != n2.val:
                return False
        return len(root1_sequence) == len(root2_sequence)
