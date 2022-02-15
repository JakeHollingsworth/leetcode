'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

class Solution:
    '''
    Potentially an abuse of python. We dynamically create an attribute 'visited' for ListNode objects that we encounter.
    From here we can just check whether the node we are at has already been visited to conclude we are in a cycle.
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if hasattr(head, 'visited'):
                return True
            head.visited = True
            head = head.next
        return False
