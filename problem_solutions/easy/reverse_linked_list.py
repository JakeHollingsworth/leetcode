'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        lagger = None
        current = head
        leader = head.next
        while leader:
            current.next = lagger
            lagger = current
            current = leader
            leader = leader.next
        current.next = lagger
        return current
