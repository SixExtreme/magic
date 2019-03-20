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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        zero = ListNode(0)
        zero.next = head

        prev, curr = zero, head
        while curr:
            if curr.val != val:
                prev, curr = curr, curr.next
            else:
                prev.next, curr = curr.next, curr.next

        return zero.next


def test_solution():
    head = build_link_list([1, 2, 6, 3, 4, 5, 6])
    assert Solution().removeElements(head, 6).to_array() == [1, 2, 3, 4, 5]

    head = build_link_list([1, 1])
    assert Solution().removeElements(head, 1) is None


if __name__ == '__main__':
    test_solution()
