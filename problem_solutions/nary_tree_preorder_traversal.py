'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''
class Solution:    
    def preorder(self, root: 'Node') -> List[int]:
        if not root: 
            return []
        return_li = [root.val]
        if not root.children:
            return return_li
        else:
            children_traversal = [self.preorder(child) for child in root.children]
            for li in children_traversal:
                return_li += li
        return return_li
