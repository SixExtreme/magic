# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(array: list):
    if len(array) == 0:
        return None
    head = curr = ListNode(array[0])
    for i in range(1, len(array)):
        curr.next = ListNode(array[i])
        curr = curr.next
    return head


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def reverse(_head: ListNode):
            curr, prev = _head, None
            while curr:
                _next = curr.next
                curr.next = prev
                curr, prev = _next, curr
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        p, q = head, reverse(slow)
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next

        return True


def test_solution():
    head = build_linked_list([1, 2])
    assert not Solution().isPalindrome(head)

    head = build_linked_list([1, 2, 2, 1])
    assert Solution().isPalindrome(head)


if __name__ == '__main__':
    test_solution()
