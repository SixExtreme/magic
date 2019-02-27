# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # solution 1
    # def maxPoints(self, points):
    #
    #     def get_gcd(a, b):
    #         while b:
    #             a, b = b, a % b
    #         return a
    #
    #     n = len(points)
    #     if n < 3:
    #         return n
    #
    #     ans, _map = 0, dict()
    #     for i in range(len(points)):
    #         _map.clear()
    #         same, _max = 1, 0
    #         for j in range(i + 1, len(points)):
    #             dx = points[j].x - points[i].x
    #             dy = points[j].y - points[i].y
    #             if dx == 0 and dy == 0:
    #                 same += 1
    #                 continue
    #             gcd = get_gcd(dx, dy)
    #             dx //= gcd
    #             dy //= gcd
    #             _map[(dx, dy)] = _map.get((dx, dy), 0) + 1
    #             _max = max(_max, _map[(dx, dy)])
    #         ans = max(ans, _max + same)
    #     return ans

    # solution 2
    def maxPoints(self, points):
        from decimal import Decimal

        n = len(points)
        if n < 3:
            return n

        ans, _map = 0, dict()
        for i in range(len(points)):
            _map.clear()
            same, _max = 1, 0
            for j in range(i + 1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                k = 'inf' if dx == 0 else Decimal(dy) / Decimal(dx)
                _map[k] = _map.get(k, 0) + 1
                _max = max(_max, _map[k])
            ans = max(ans, _max + same)
        return ans


def test_solution():
    points = [Point(1, 1), Point(2, 2), Point(3, 3)]
    assert Solution().maxPoints(points) == 3
    
    points = [Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]
    assert Solution().maxPoints(points) == 2


if __name__ == '__main__':
    test_solution()
