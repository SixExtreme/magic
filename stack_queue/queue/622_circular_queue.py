# class MyCircularQueue:
#
#     def __init__(self, k):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         :type k: int
#         """
#         self.queue = [0] * k
#         self.size, self.count = k, 0
#         self.head, self.tail = -1, -1
#
#     def enQueue(self, value):
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         :type value: int
#         :rtype: bool
#         """
#         if self.count == self.size:
#             return False
#
#         if self.count == 0:
#             self.head = 0
#         self.tail = (self.tail + 1) % self.size
#
#         self.count += 1
#         self.queue[self.tail] = value
#
#         return True
#
#     def deQueue(self):
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         :rtype: bool
#         """
#         if self.count == 0:
#             return False
#
#         self.count -= 1
#         self.queue[self.head] = 0
#
#         self.head = (self.head + 1) % self.size
#         if self.count == 0:
#             self.head, self.tail = -1, -1
#
#         return True
#
#     def Front(self):
#         """
#         Get the front item from the queue.
#         :rtype: int
#         """
#         if self.count == 0:
#             return -1
#         return self.queue[self.head]
#
#     def Rear(self):
#         """
#         Get the last item from the queue.
#         :rtype: int
#         """
#         if self.count == 0:
#             return -1
#         return self.queue[self.tail]
#
#     def isEmpty(self):
#         """
#         Checks whether the circular queue is empty o r not.
#         :rtype: bool
#         """
#         return self.count == 0
#
#     def isFull(self):
#         """
#         Checks whether the circular queue is full or not.
#         :rtype: bool
#         """
#         return self.count == self.size


# class MyCircularQueue:
#
#     def __init__(self, k):
#         """
#         Initialize your data structure here. Set the size of the queue to be k.
#         :type k: int
#         """
#         self.queue = [0] * k
#         self.head, self.tail = 0, 0
#         self.size, self.count = k, 0
#
#     def enQueue(self, value):
#         """
#         Insert an element into the circular queue. Return true if the operation is successful.
#         :type value: int
#         :rtype: bool
#         """
#         if self.count == self.size:
#             return False
#
#         if self.count != 0:
#             self.tail = (self.tail + 1) % self.size
#
#         self.count += 1
#         self.queue[self.tail] = value
#
#         return True
#
#     def deQueue(self):
#         """
#         Delete an element from the circular queue. Return true if the operation is successful.
#         :rtype: bool
#         """
#         if self.count == 0:
#             return False
#
#         self.count -= 1
#         self.queue[self.head] = 0
#
#         self.head = (self.head + 1) % self.size
#         if self.count == 0:
#             self.head, self.tail = 0, 0
#
#         return True
#
#     def Front(self):
#         """
#         Get the front item from the queue.
#         :rtype: int
#         """
#         if self.count == 0:
#             return -1
#         return self.queue[self.head]
#
#     def Rear(self):
#         """
#         Get the last item from the queue.
#         :rtype: int
#         """
#         if self.count == 0:
#             return -1
#         return self.queue[self.tail]
#
#     def isEmpty(self):
#         """
#         Checks whether the circular queue is empty o r not.
#         :rtype: bool
#         """
#         return self.count == 0
#
#     def isFull(self):
#         """
#         Checks whether the circular queue is full or not.
#         :rtype: bool
#         """
#         return self.count == self.size


class MyCircularQueue:

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.queue = [0] * k
        self.head, self.tail = -1, -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        if self.head == self.tail:
            self.head, self.tail = -1, -1
        else:
            self.head = (self.head + 1) % self.size

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty o r not.
        :rtype: bool
        """
        return self.head == -1

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.tail + 1) % self.size == self.head

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

def test_solution():
    queue = MyCircularQueue(3)

    assert queue.enQueue(2)
    assert queue.Front() == 2
    assert queue.Rear() == 2
    assert queue.deQueue()
    assert queue.Front() == -1
    assert not queue.deQueue()
    assert queue.Front() == -1
    assert queue.enQueue(4)
    assert queue.enQueue(2)
    assert queue.enQueue(2)
    assert not queue.enQueue(3)
