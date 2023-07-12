"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by
continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def has_cycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

    def has_cycle_alt(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while p1:
            p1 = p1.next
            if p1 is None:
                break
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return True
        return False


def print_linked_list_as_str(head: ListNode):
    pointer = head
    nodes = []
    while pointer:
        nodes.append(str(pointer.val))
        pointer = pointer.next
    print("-->".join(nodes))


def print_linked_list_as_list(head: ListNode):
    nodes_values = []
    while head:
        nodes_values.append(head.val)
        head = head.next
    print(nodes_values)


if __name__ == '__main__':
    # nodes
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    # create a linked list of nodes without cycle
    # ll_without_cycle = n1
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    # n5.next = n6
    # print_linked_list_as_list(ll_without_cycle)

    # create a linked list of nodes with cycle
    ll_with_cycle = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3

    sol = Solution()
    print(sol.has_cycle_alt(ll_with_cycle))
