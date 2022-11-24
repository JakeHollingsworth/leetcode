'''
Given the head of a singly linked list, return true if it is a palindrome.
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        n = 0
        running_node = head
        while running_node:
            n += 1
            running_node = running_node.next
        lagger = None
        current = head
        leader = head.next
        i = 0
        # Reverse first half of list and compare to second half for O(1) space
        while i < n // 2:
            current.next = lagger
            lagger = current
            current = leader
            leader = current.next
            i += 1
        backwards, forwards = (lagger, current) if not n % 2 else (lagger, current.next)
        while backwards and forwards:
            if backwards.val != forwards.val:
                return False
            backwards, forwards = backwards.next, forwards.next
        return True if not backwards and not forwards else False
