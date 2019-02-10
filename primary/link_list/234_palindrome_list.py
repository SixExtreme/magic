# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # solution 1
        # nums = []
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        #
        # if len(nums) < 2:
        #     return True
        #
        # i, j = 0, len(nums) - 1
        # while i < j:
        #     if nums[i] != nums[j]:
        #         return False
        #     i, j = i + 1, j - 1
        # return True

        # solution 2
        def reverse(h: ListNode) -> ListNode:
            prev = None
            while h:
                next = h.next
                h.next = prev
                prev, h = h, next
            return prev

        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next if fast else slow

        p, q = head, reverse(slow)
        while q:
            if p.val != q.val:
                return False
            p, q = p.next, q.next

        return True


def test_solution():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    assert Solution().isPalindrome(head)

    head.next.next = ListNode(3)
    assert not Solution().isPalindrome(head)

    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    assert Solution().isPalindrome(head)



