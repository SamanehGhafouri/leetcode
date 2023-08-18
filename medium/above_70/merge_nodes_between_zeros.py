"""
You are given the head of a linked list, which contains a series of integers separated by 0's.
The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value
is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
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

    def merge_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        list_node = h
        sum_num = 0
        while head.next is not None:
            node_val = head.next.val
            if node_val != 0:
                sum_num += int(node_val)
            elif node_val == 0:
                h.next = ListNode(sum_num)
                h = h.next
                sum_num = 0
            head = head.next
        print(self.print_linked_list(list_node.next))


if __name__ == '__main__':
    # head = [0, 3, 1, 0, 4, 5, 2, 0]
    nl1 = ListNode(0)
    nl2 = ListNode(3)
    nl3 = ListNode(1)
    nl4 = ListNode(0)
    nl5 = ListNode(4)
    nl6 = ListNode(5)
    nl7 = ListNode(2)
    nl8 = ListNode(0)

    lls1 = nl1
    nl1.next = nl2
    nl2.next = nl3
    nl3.next = nl4
    nl4.next = nl5
    nl5.next = nl6
    nl6.next = nl7
    nl7.next = nl8

    ####################
    obj = Solution()
    print(obj.merge_nodes(lls1))
