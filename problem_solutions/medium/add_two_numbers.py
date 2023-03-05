'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        head = ans
        while l1 and l2:
            total = l1.val + l2.val + carry
            ans.val = total % 10
            carry = total // 10
            l1, l2 = l1.next, l2.next
            if l1 or l2 or carry:
                ans.next = ListNode()
                ans = ans.next
        while l1 or l2:
            # rename lists so that l1 is non-None
            l1 = l2 if l2 else l1
            l2 = None
            total = l1.val + carry
            ans.val = total % 10
            carry = total // 10
            l1 = l1.next
            if l1 or carry:
                ans.next = ListNode()
                ans = ans.next
        if carry:
            ans.val = carry
        return head
