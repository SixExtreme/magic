# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def array_to_linklist(array: list) -> Node:
    if len(array) == 0:
        return None
    head = prev = Node(array[0], None, None, None)
    for i in range(1, len(array)):
        node = Node(array[i], None, None, None)
        node.prev = prev
        prev.next = node
        prev = node
    return head


def linklist_to_array(head: Node) -> list:
    array = []
    if not head:
        return array
    p = head
    while p:
        array.append(p.val)
        p = p.next
    return array


class Solution:
    def flatten(self, head: Node) -> Node:
        if head is None:
            return head
        p, stack = head, []
        while p:
            if p.child:
                if p.next:
                    stack.append(p.next)
                    p.next.prev = None
                p.next = p.child
                p.next.prev = p
                p.child = None
            if stack and p.next is None:
                p.next = stack.pop()
                p.next.prev = p
            p = p.next
        return head


def test_transform():
    array = [1, 2, 3, 4, 5]
    assert array == linklist_to_array(array_to_linklist(array))


def test_solution():
    head1 = array_to_linklist([0, 1, 9])
    head2 = array_to_linklist([2, 5])
    head3 = array_to_linklist([3, 4])
    head4 = array_to_linklist([6, 7, 8])

    head2.child = head3
    head2.next.child = head4
    head1.next.child = head2

    head = Solution().flatten(head1)
    assert linklist_to_array(head) == list(range(10))




