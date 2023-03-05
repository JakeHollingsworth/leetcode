'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        head = head
        prev = head
        runner = head.next
        end = head
        for i in range(n):
            end = end.next
        while end and end.next:
            prev = prev.next
            runner = runner.next
            end = end.next
        if not end:
            return head.next
        prev.next = runner.next
        return head

