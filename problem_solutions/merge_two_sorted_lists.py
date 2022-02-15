'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        running_node = ListNode(0)
        head = running_node
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    running_node.next = list1
                    list1 = list1.next
                else:
                    running_node.next = list2
                    list2 = list2.next
                running_node = running_node.next
            else:
                list1, list2 = list1, list2 if list1 else list2, None
                while list1:
                    running_node.next = list1
                    list1 = list1.next
                    running_node = running_node.next
        return head.next
