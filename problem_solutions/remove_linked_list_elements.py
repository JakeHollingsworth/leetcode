'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        while head and head.val == val:
            head = head.next
        running_node = head
        while running_node:
            if running_node.next and running_node.next.val == val:
                running_node.next = running_node.next.next
            else:
                running_node = running_node.next
        return head
