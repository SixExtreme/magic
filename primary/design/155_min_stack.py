import bisect

# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.order = []
#
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: void
#         """
#         self.stack.append(x)
#         bisect.insort(self.order, x)
#
#     def pop(self):
#         """
#         :rtype: void
#         """
#         if len(self.stack) == 0:
#             return
#
#         x = self.stack.pop()
#         self.order.remove(x)
#         return x
#
#     def top(self):
#         """
#         :rtype: int
#         """
#         if len(self.stack) == 0:
#             return
#         return self.stack[-1]
#
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         if len(self.order) == 0:
#             return
#         return self.order[0]


class MinStack:

    # stack中存放实际值和最小值的差值
    # 压入或弹出负值时，最小值发生变化

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = 0
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            return
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


def test_solution():
    ms = MinStack()

    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3

    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
