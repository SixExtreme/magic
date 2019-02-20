class MinStack:

    # stack中存放实际值和最小值的差值
    # 压入或弹出负值时，最小值发生变化

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min, self._stack = 0, []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self._stack) == 0:
            self._min = x
            self._stack.append(0)
        else:
            self._stack.append(x - self._min)
            self._min = min(self._min, x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self._stack) == 0:
            return
        peek = self._stack.pop()
        if peek < 0:
            _min = self._min
            self._min -= peek
            return _min
        return peek + self._min

    def top(self):
        """
        :rtype: int
        """
        if len(self._stack) == 0:
            return
        if self._stack[-1] < 0:
            return self._min
        return self._min + self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min


def test_solution():
    ms = MinStack()

    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3

    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
