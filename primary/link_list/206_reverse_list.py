# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def to_array(self):
        p, arr = self, []
        while p:
            arr.append(p.val)
            p = p.next
        return arr


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head:
        #     return head
        # prev, p, q = None, head, head.next
        # while q:
        #     r = q.next
        #     p.next, q.next = prev, p
        #     prev, p, q = p, q, r
        # return p

        if not head:
            return head
        p, q = None, head
        while q:
            next = q.next
            q.next = p
            p, q = q, next
        return p


def test_solution():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    assert head.to_array() == [0, 1, 2, 3, 4]

    tail = Solution().reverseList(head)
    assert tail.to_array() == [4, 3, 2, 1, 0]

