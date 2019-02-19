from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: 'int') -> 'None':
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> 'int':
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.queue) == 0:
            return -1
        return self.queue.popleft()

    def top(self) -> 'int':
        """
        Get the top element.
        """
        if len(self.queue) == 0:
            return -1
        return self.queue[0]

    def empty(self) -> 'bool':
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


def test_solution():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.top() == 1
    assert not stack.empty()
