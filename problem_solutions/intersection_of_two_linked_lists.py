'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        running_node = headA
        lenA = 0
        while running_node:
            lenA += 1
            running_node = running_node.next
        running_node = headB
        lenB = 0
        while running_node:
            lenB += 1
            running_node = running_node.next
        # A and B must end on the same node if they intersect.
        long, short = (headA, headB) if lenA > lenB else (headB, headA)
        lenShort, lenLong = min(lenA, lenB), max(lenA, lenB)
        # Run along the longest list until it has the same number of remaining elements.
        for i in range(lenShort, lenLong):
            long = long.next
        for i in range(lenShort):
            if long == short:
                return long
            long = long.next
            short = short.next
        return None
