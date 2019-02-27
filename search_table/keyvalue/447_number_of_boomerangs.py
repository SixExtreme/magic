class Solution:
    def numberOfBoomerangs(self, points: 'List[List[int]]') -> int:
        ans = 0

        n, _map = len(points), dict()
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
                _map[distance] = _map.get(distance, 0) + 1

            for val in _map.values():
                ans += val * (val - 1)
            _map.clear()

        return ans


def test_solution():
    points = [[0, 0], [1, 0], [2, 0]]
    assert Solution().numberOfBoomerangs(points) == 2
