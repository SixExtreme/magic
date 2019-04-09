# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def array_to_linklist(array: list) -> ListNode:
    if len(array) == 0:
        return None
    head = p = ListNode(array[0])
    for i in range(1, len(array)):
        p.next = ListNode(array[i])
        p = p.next
    return head


def linklist_to_array(head: ListNode) -> list:
    array = []
    if head is None:
        return array
    p = head
    while p:
        array.append(p.val)
        p = p.next
    return array


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # solution 1
        # if head is None:
        #     return head
        #
        # p, length = head, 0
        # while p:
        #     length += 1
        #     p = p.next
        #
        # k %= length
        # if k == 0:
        #     return head
        #
        # p = head
        # for _ in range(length - k - 1):
        #     p = p.next
        #
        # ans, p.next = p.next, None
        #
        # q = ans
        # while q.next:
        #     q = q.next
        # q.next = head
        #
        # return ans

        # solution 2
        if head is None:
            return head

        p, length = head, 1
        while p.next:
            p = p.next
            length += 1
        p.next = head

        k %= length
        if k != 0:
            for _ in range(length - k):
                p = p.next
        ans, p.next = p.next, None
        return ans


def test_solution():
    head = array_to_linklist([1, 2, 3, 4, 5])
    head = Solution().rotateRight(head, 2)
    assert linklist_to_array(head) == [4, 5, 1, 2, 3]

    head = array_to_linklist([0, 1, 2])
    head = Solution().rotateRight(head, 4)
    assert linklist_to_array(head) == [2, 0, 1]
