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


def build_link_list(array: list):
    zero = ListNode(0)
    p = zero
    for x in array:
        p.next = ListNode(x)
        p = p.next
    return zero.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q = l1, l2
        head = ListNode(0)

        cur, cry = head, 0
        while p or q:
            if p:
                cry += p.val
                p = p.next
            if q:
                cry += q.val
                q = q.next

            cur.next = ListNode(cry % 10)
            cur, cry = cur.next, cry // 10
        if cry != 0:
            cur.next = ListNode(cry)

        return head.next


def test_solution():
    l1 = build_link_list([2, 4, 3])
    l2 = build_link_list([5, 6, 4])
    assert Solution().addTwoNumbers(l1, l2).to_array() == [7, 0, 8]


if __name__ == '__main__':
    test_solution()
