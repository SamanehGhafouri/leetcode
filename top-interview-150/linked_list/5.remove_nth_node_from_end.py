"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
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

    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        len_list = 0
        tail = head
        temp_1 = head
        while tail.next is not None:
            tail = tail.next
            len_list += 1
        len_list += 1
        if len_list == 1 and n == 1:
            return None
        diff = len_list - n
        if diff != 0:
            while diff > 1:
                temp_1 = temp_1.next
                diff -= 1
            temp_2 = temp_1.next.next
            temp_3 = temp_1.next
            temp_3.next = None
            temp_1.next = temp_2
            self.print_linked_list(head)
        else:
            self.print_linked_list(head.next)
if __name__ == '__main__':
    nl1 = ListNode(1)
    nl2 = ListNode(2)
    nl3 = ListNode(3)
    nl4 = ListNode(4)
    nl5 = ListNode(5)

    lls1 = nl1
    nl1.next = nl2
    nl2.next = nl3
    nl3.next = nl4
    nl4.next = nl5
    ###################
    nl5 = ListNode(1)
    nl6 = ListNode(3)
    nl7 = ListNode(4)

    lls2 = nl5
    nl5.next = nl6
    nl6.next = nl7
    ####################
    obj = Solution()
    print(obj.remove_nth_from_end(lls1, 5))

    # l1 = [1, 2, 3, 4, 5]
    # n = 2
    # expected = [1, 2, 3, 5]
