class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = ListNode(-1)
        self.tail = self.head

    def to_list(self):
        vals, p = [], self.head.next
        while p:
            vals.append(p.val)
            p = p.next
        return vals

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        elif index == 0:
            return self.head.next.val
        elif index == self.length - 1:
            return self.tail.val
        else:
            p = self.head.next
            for _ in range(index):
                p = p.next
            return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        if self.length == 0:
            self.tail = node

        node.next = self.head.next
        self.head.next = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended
        to the end of linked list. If index is greater than the length,
        the node will not be inserted.
        """
        if index > self.length:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            p = self.head
            for _ in range(index):
                p = p.next

            node = ListNode(val)
            node.next = p.next
            p.next = node

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        p = self.head
        for _ in range(index):
            p = p.next

        p.next = p.next.next
        if p.next is None:
            self.tail = p

        self.length -= 1


def test_solution():
    link = MyLinkedList()

    link.addAtHead(0)
    assert link.get(0) == 0
    assert link.length == 1

    link.addAtIndex(1, 9)
    assert link.get(1) == 9
    assert link.length == 2

    link.addAtIndex(1, 5)
    assert link.get(1) == 5
    assert link.length == 3

    link.addAtTail(7)
    assert link.get(3) == 7
    assert link.length == 4

    link.addAtHead(1)
    assert link.get(0) == 1
    assert link.length == 5

    link.addAtIndex(5, 8)
    assert link.get(5) == 8
    assert link.length == 6

    link.addAtIndex(5, 2)
    assert link.get(5) == 2
    assert link.length == 7

    link.addAtIndex(3, 0)
    assert link.get(3) == 0
    assert link.length == 8

    link.addAtTail(1)
    assert link.get(8) == 1
    assert link.length == 9

    link.addAtTail(0)
    assert link.get(9) == 0
    assert link.length == 10

    link.deleteAtIndex(6)
    assert link.get(6) == 8
    assert link.length == 9
