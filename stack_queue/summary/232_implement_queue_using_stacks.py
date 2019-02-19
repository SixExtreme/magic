# class MyQueue:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x: 'int') -> 'None':
#         """
#         Push element x to the back of queue.
#         """
#         array = []
#         while self.stack:
#             array.append(self.stack.pop())
#         self.stack.append(x)
#         while array:
#             self.stack.append(array.pop())
#
#     def pop(self) -> 'int':
#         """
#         Removes the element from in front of queue and returns that element.
#         """
#         if len(self.stack) == 0:
#             return -1
#         return self.stack.pop()
#
#     def peek(self) -> 'int':
#         """
#         Get the front element.
#         """
#         if len(self.stack) == 0:
#             return -1
#         return self.stack[-1]
#
#     def empty(self) -> 'bool':
#         """
#         Returns whether the queue is empty.
#         """
#         return len(self.stack) == 0

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ipt, self.opt = [], []

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        self.ipt.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        if len(self.opt) == 0:
            return -1
        return self.opt.pop()

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        if len(self.opt) == 0:
            while self.ipt:
                self.opt.append(self.ipt.pop())
        if len(self.opt) == 0:
            return -1
        return self.opt[-1]

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return len(self.ipt) == 0 and len(self.opt) == 0


def test_solution():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert not queue.empty()
