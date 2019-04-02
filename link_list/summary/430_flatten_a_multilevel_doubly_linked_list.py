# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def array_to_linklist(array: list) -> Node:
    if len(array) == 0:
        return Node
    head = prev = Node(array[0], None, None, None)
    for i in range(1, len(array)):
        node = Node(array[i], None, None, None)
        prev.next = node
        node.prev = prev
        prev = node
    return head


def linklist_to_array(head: Node) -> list:
    array = []
    if head is None:
        return array
    p = head
    while p:
        array.append(p.val)
        p = p.next
    return array


class Solution:
    def flatten(self, head: Node) -> Node:
        # solution 1
        # if head is None:
        #     return head
        # p, stack = head, []
        # while p:
        #     if p.child:
        #         if p.next:
        #             stack.append(p.next)
        #             p.next.prev = None
        #         p.next = p.child
        #         p.next.prev = p
        #         p.child = None
        #     if stack and p.next is None:
        #         p.next = stack.pop()
        #         p.next.prev = p
        #     p = p.next
        # return head

        # solution 2
        if head is None:
            return head
        p = head
        while p:
            if p.child is None:
                p = p.next
            else:
                q = p.child
                while q.next:
                    q = q.next
                q.next = p.next
                if p.next:
                    p.next.prev = q
                p.next = p.child
                p.next.prev = p
                p.child = None
        return head


def test_transform():
    array = [1, 2, 3, 4, 5]
    return array == linklist_to_array(array_to_linklist(array))


def test_solution():
    head = array_to_linklist([1, 2, 6])
    head.next.child = array_to_linklist([3, 4, 5])
    head.next.child.next.child = array_to_linklist([-4, -5])
    head.next.next.child = array_to_linklist([7, 8, 9])
    assert linklist_to_array(Solution().flatten(head)) == [1, 2, 3, 4, -4, -5, 5, 6, 7, 8, 9]


