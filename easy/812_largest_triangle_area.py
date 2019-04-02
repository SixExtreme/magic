from typing import List
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        # solution 1
        # ans = 0
        # for i in range(len(points) - 2):
        #     for j in range(i + 1, len(points) - 1):
        #         for k in range(j + 1, len(points)):
        #             x1, y1 = points[i]
        #             x2, y2 = points[j]
        #             x3, y3 = points[k]
        #             s = abs(0.5 * (x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2))
        #             ans = max(ans, s)
        # return ans

        # solution 2
        ans = 0
        for item in combinations(range(len(points)), 3):
            i, j, k = item
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            ans = max(ans, abs(0.5 * (x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2)))
        return ans



def test_solution():
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    assert Solution().largestTriangleArea(points) == 2.0
