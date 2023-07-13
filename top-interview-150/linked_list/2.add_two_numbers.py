"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
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

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_dummy = ''
        l2_dummy = ''

        while l1:
            l1_dummy += str(l1.val)
            l1 = l1.next

        while l2:
            l2_dummy += str(l2.val)
            l2 = l2.next

        result_lls = str(int(l1_dummy[::-1]) + int(l2_dummy[::-1]))[::-1]
        final_lls = ListNode(int(result_lls[0]))
        i = 1
        while len(result_lls):
            if i == len(result_lls):
                break
            self.insert(final_lls, int(result_lls[-i]))
            i += 1
        print(self.print_linked_list(final_lls))
        return final_lls

    def add_two_numbers_faster(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(None)
        p3 = l3
        carry_over = 0

        while l1 and l2:
            s = l1.val + l2.val + carry_over
            carry_over = s // 10
            p3.next = ListNode(s % 10)
            l1 = l1.next
            l2 = l2.next
            p3 = p3.next

        while l1:
            s = l1.val + carry_over
            carry_over = s // 10
            p3.next = ListNode(s % 10)
            l1 = l1.next
            p3 = p3.next

        while l2:
            s = l1.val + carry_over
            carry_over = s // 10
            p3.next = ListNode(s % 10)
            l2 = l2.next
            p3 = p3.next

        p3.next = ListNode(carry_over)
        print(self.print_linked_list(l3.next))
        return l3.next


if __name__ == '__main__':
    nl1 = ListNode(9)
    nl2 = ListNode(9)
    nl3 = ListNode(9)
    nl4 = ListNode(9)

    lls1 = nl1
    nl1.next = nl2
    nl2.next = nl3
    nl3.next = nl4
    ###################
    nl5 = ListNode(9)
    nl6 = ListNode(9)
    nl7 = ListNode(9)

    lls2 = nl5
    nl5.next = nl6
    nl6.next = nl7
    ####################
    obj = Solution()
    print(obj.add_two_numbers_faster(lls1, lls2))

    # l1 = [9, 9, 9, 9]
    # l2 = [9, 9, 9]
