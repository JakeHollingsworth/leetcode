'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        new_head = ListNode(0, head)
        prev = new_head
        first = head
        second = head.next
        while second:
            next_pair = second.next
            second.next = first
            prev.next = second
            first.next = next_pair

            prev = first
            first = prev.next
            if first:
                second = first.next
            else:
                second = None
        return new_head.next
