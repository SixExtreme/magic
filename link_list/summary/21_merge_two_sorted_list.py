# Definition for singly-linked list.
class ListNode(object):

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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)

        curr, p, q = head, l1, l2
        while p or q:
            if p and q:
                if p.val < q.val:
                    curr.next = p
                    p = p.next
                else:
                    curr.next = q
                    q = q.next
            elif p:
                curr.next = p
                p = p.next
            else:
                curr.next = q
                q = q.next
            curr = curr.next
        return head.next


def test_solution():
    l1 = build_link_list([1, 2, 4])
    l2 = build_link_list([1, 3, 4])
    head = Solution().mergeTwoLists(l1, l2)
    assert head.to_array() == [1, 1, 2, 3, 4, 4]

