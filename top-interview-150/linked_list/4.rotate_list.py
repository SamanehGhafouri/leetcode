"""
Given the head of a linked list, rotate the list to the right by k places.
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

    def rotate_right(self, head: Optional[ListNode], k: int):
        if head is None:
            return None

        count = 1
        tail = head

        # find end of linked list and count the number of nodes
        while tail.next is not None:
            tail = tail.next
            count += 1

        # create linked list cycle
        tail.next = head

        # finding the difference between count and k
        k = k % count
        diff = count - k

        # move the head to one position before the new head
        while diff > 1:
            head = head.next
            diff -= 1

        # cut the cycle and set the new head
        temp = head.next
        head.next = None
        self.print_linked_list(temp)
        return temp


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
    print(obj.rotate_right(lls1, 2))

    # l1 = [1, 2, 3, 4, 5]
    # expected = [4, 5, 1, 2, 3]
