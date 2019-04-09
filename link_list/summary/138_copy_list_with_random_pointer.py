# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def build_linklist(array: list, hmap: dict) -> Node:
    if len(array) == 0:
        return None
    _list = [Node(array[0], None, None)]

    head = p = _list[0]
    for i in range(1, len(array)):
        p.next = Node(array[i], None, None)
        _list.append(p.next)
        p = p.next

    for ia, ib in hmap.items():
        _list[ia].random = _list[ib]
    return head


def reverse_design(head: Node) -> (list, dict):
    array = []
    if head is None:
        return array

    idx, p, node_to_index = 0, head, dict()
    while p:
        array.append(p.val)
        node_to_index[p] = idx
        idx += 1
        p = p.next

    relation = dict()
    for node, idx in node_to_index.items():
        if node.random:
            relation[idx] = node_to_index[node.random]
    return array, relation


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return head

        node = Node(head.val, None, None)
        _hmap, _list = {head: 0}, [node]

        idx, p, q = 1, head, node
        while p.next:
            q.next = Node(p.next.val, None, None)
            _hmap[p.next] = idx
            _list.append(q.next)
            idx += 1
            p, q = p.next, q.next

        p, q = head, node
        while p:
            if p.random:
                idx = _hmap[p.random]
                q.random = _list[idx]
            q = q.next
            p = p.next
        return node


def test_transform():
    array, hmap = [1, 2], {0: 1, 1: 1}
    assert reverse_design(build_linklist(array, hmap)) == (array, hmap)


def test_solution():
    array, hmap = [1, 2], {0: 1, 1: 1}
    origin = build_linklist(array, hmap)
    target = Solution().copyRandomList(origin)
    assert reverse_design(target) == (array, hmap)


if __name__ == '__main__':
    test_solution()
