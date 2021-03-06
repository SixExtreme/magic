# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
            if slow is fast:
                return True
        return False


def test_solution():
    head1 = ListNode(0)
    head1.next = ListNode(1)
    head1.next.next = head1
    assert Solution().hasCycle(head1)

    head2 = ListNode(0)
    head2.next = ListNode(1)
    assert not Solution().hasCycle(head2)
