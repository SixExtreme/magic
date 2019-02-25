# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points: 'List[Point]') -> 'int':
        n, _map = len(points), dict()
        if n < 3:
            return n

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i].x, points[i].y
                x2, y2 = points[j].x, points[j].y

                k, b = None, None
                if x1 == x2:
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1

                if (k, b) not in _map:
                    _map[(k, b)] = {i, j}
                else:
                    _map[(k, b)].add(i)
                    _map[(k, b)].add(j)

        return max(len(s) for s in _map.values())


def test_solution():
    points = [Point(1, 1), Point(2, 2), Point(3, 3)]
    assert Solution().maxPoints(points) == 3
