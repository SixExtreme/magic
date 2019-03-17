# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # solution 1
        # p, q = headA, headB
        # if p is q:
        #     return p
        #
        # l1, l2 = 0, 0
        # while p or q:
        #     if p:
        #         p = p.next
        #         l1 += 1
        #     if q:
        #         q = q.next
        #         l2 += 1
        #
        # p, q = headA, headB
        # if l1 < l2:
        #     p, q = q, p
        #
        # delt = abs(l1 - l2)
        # for _ in range(delt):
        #     p = p.next
        #
        # while p is not q:
        #     p = p.next
        #     q = q.next
        # return p

        # solution 2
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


def test_solution():
    headA = ListNode(1)
    headA.next = ListNode(2)

    headB = ListNode(3)

    node = ListNode(4)
    node.next = ListNode(5)

    headA.next.next = node
    headB.next = node

    assert Solution().getIntersectionNode(headA, headB) is node

    headA = ListNode(6)
    headB = ListNode(7)

    assert Solution().getIntersectionNode(headA, headB) is None
