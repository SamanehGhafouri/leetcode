"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def print_linked_list(self, head: ListNode):
        node_values = []
        while head:
            node_values.append(str(head.val))
            head = head.next
        print(print(node_values))

    def merge_two_sorted_list(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        p3 = list3
        while list1 and list2:
            if list1.val <= list2.val:
                p3.next = ListNode(list1.val)
                list1 = list1.next
                p3 = p3.next
            elif list1.val > list2.val:
                p3.next = ListNode(list2.val)
                list2 = list2.next
                p3 = p3.next

        while list1:
            p3.next = ListNode(list1.val)
            list1 = list1.next
            p3 = p3.next

        while list2:
            p3.next = ListNode(list2.val)
            list2 = list2.next
            p3 = p3.next

        print(self.print_linked_list(list3.next))
        return list3.next


if __name__ == '__main__':
    nl1 = ListNode(1)
    nl2 = ListNode(2)
    nl3 = ListNode(4)

    lls1 = nl1
    nl1.next = nl2
    nl2.next = nl3
    ###################
    nl5 = ListNode(1)
    nl6 = ListNode(3)
    nl7 = ListNode(4)

    lls2 = nl5
    nl5.next = nl6
    nl6.next = nl7
    ####################
    obj = Solution()
    print(obj.merge_two_sorted_list(lls1, lls2))

    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]
    # return [1, 1, 2, 3, 4, 4
