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


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        odd, even = head, head.next

        times, p, q = 0, odd, even
        while p.next and q.next:
            p.next = q.next
            p = p.next
            p, q = q, p
            times += 1

        if times % 2 == 0:
            p.next = even
        else:
            p.next = None
            q.next = even
        return odd


def test_solution():
    head = build_link_list([1, 2, 3, 4])
    ans = Solution().oddEvenList(head)
    assert ans.to_array() == [1, 3, 2, 4]

    head = build_link_list([1, 2, 3, 4, 5])
    ans = Solution().oddEvenList(head)
    assert ans.to_array() == [1, 3, 5, 2, 4]

    head = build_link_list([2, 1, 3, 5, 6, 4, 7])
    ans = Solution().oddEvenList(head)
    assert ans.to_array() == [2, 3, 6, 7, 1, 5, 4]
