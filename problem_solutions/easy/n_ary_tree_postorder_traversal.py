'''
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        return_li = [root.val]
        if not root.children:
            return return_li
        for node in root.children[::-1]:
            child_traversal = self.postorder(node)
            return_li = child_traversal + return_li
        return return_li
