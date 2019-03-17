# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # k: start -> meet
        # r: length of cycle
        # s: start -> cycle
        # m: cycle -> meet

        # 2k - k = nr
        # k = nr
        # s = k - m
        # s = nr - m

        if not head or not head.next:
            return None

        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            if not fast.next:
                return None
            fast = fast.next.next
            if slow is fast:
                break

        if slow is not fast:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow


def test_solution():
    head1 = ListNode(0)
    head1.next = ListNode(1)
    head1.next.next = head1
    assert Solution().detectCycle(head1) is head1

    head2 = ListNode(0)
    head2.next = ListNode(1)
    assert Solution().detectCycle(head2) is None

    head3 = ListNode(1)
    head3.next = ListNode(2)
    head3.next.next = ListNode(3)
    head3.next.next.next = ListNode(4)
    head3.next.next.next.next = head3.next
    assert Solution().detectCycle(head3) is head3.next

