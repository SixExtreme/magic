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
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        # solution 1
        # if not head:
        #     return head
        #
        # p = head
        # for i in range(n):
        #     p = p.next
        # if not p:
        #     return head.next
        #
        # q = head
        # while p.next:
        #     p, q = p.next, q.next
        #
        # q.next = q.next.next
        #
        # return head

        # solution 2
        if not head:
            return head

        start = ListNode(-1)
        start.next = head

        fast = start
        for i in range(n + 1):
            # beacuse of head, jump n+1 times
            fast = fast.next

        slow = start
        while fast:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return start.next


def test_solution():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    Solution().removeNthFromEnd(head, 2)
    assert head.to_array() == [1, 2, 3, 5]
