'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        running_node = head
        while running_node.next:
            while running_node.next and running_node.val == running_node.next.val:
                running_node.next = running_node.next.next
            if running_node.next:
                running_node = running_node.next
        return head
