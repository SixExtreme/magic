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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        zero = ListNode(0)
        zero.next = head

        slow, fast = zero, zero
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return zero.next


def test_solution():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    Solution().removeNthFromEnd(head, 2)
    assert head.to_array() == [1, 2, 3, 5]
