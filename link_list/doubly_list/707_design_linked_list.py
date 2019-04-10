class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.curr = None
        self.head = self.tail = ListNode(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        return self.get_node(index).val

    def get_node(self, index) -> ListNode:
        # 针对双向链表特性对查找指定节点进行优化
        if index >= self.length:
            return None
        if index == 0:
            return self.head.next
        elif index == self.length - 1:
            return self.tail
        elif index > self.length // 2:
            p = self.tail
            for _ in range(self.length - index - 1):
                p = p.prev
            return p
        else:
            p = self.head.next
            for _ in range(index):
                p = p.next
            return p

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        node.prev = self.head
        node.next = self.head.next

        node.prev.next = node
        if not node.next:
            self.tail = node
        else:
            node.next.prev = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            # p = self.head
            # for _ in range(index):
            #     p = p.next
            p = self.get_node(index - 1)

            node = ListNode(val)
            node.prev = p
            node.next = p.next
            node.prev.next = node
            node.next.prev = node

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            # p = self.head.next
            # for _ in range(index):
            #     p = p.next
            p = self.get_node(index)

            p.prev.next = p.next
            p.next.prev = p.prev

        self.length -= 1


def test_solution():
    link = MyLinkedList()

    link.addAtHead(5)
    assert link.length == 1
    assert link.get(0) == 5  # 5

    link.addAtHead(2)
    assert link.length == 2
    assert link.get(0) == 2  # 2, 5

    link.deleteAtIndex(1)
    assert link.length == 1  # 2

    link.addAtIndex(1, 9)
    assert link.length == 2
    assert link.get(1) == 9  # 2, 9

    link.addAtHead(4)
    assert link.length == 3
    assert link.get(0) == 4  # 4, 2, 9

    link.addAtHead(9)
    assert link.length == 4
    assert link.get(0) == 9  # 9, 4, 2, 9

    link.addAtHead(8)
    assert link.length == 5
    assert link.get(0) == 8  # 8, 9, 4, 2, 9

    assert link.get(3) == 2

    link.addAtTail(1)
    assert link.length == 6
    assert link.get(5) == 1  # 8, 9, 4, 2, 9, 1

    link.addAtIndex(3, 6)
    assert link.length == 7  # 8, 9, 4, 6, 2, 9, 1
    assert link.get(3) == 6

    link.addAtHead(3)
    assert link.length == 8
    assert link.get(0) == 3  # 3, 8, 9, 4, 6, 2, 9, 1


if __name__ == '__main__':
    test_solution()
