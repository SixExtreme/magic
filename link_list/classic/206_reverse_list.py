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
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev


def test_solution():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    assert head.to_array() == [0, 1, 2, 3, 4]

    tail = Solution().reverseList(head)
    assert tail.to_array() == [4, 3, 2, 1, 0]


