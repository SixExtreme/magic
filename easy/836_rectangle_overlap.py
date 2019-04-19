from typing import List


class Solution:
    # solution 1
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        p1, q1, p2, q2 = rec2

        LR = False if x2 <= p1 or p2 <= x1 else True
        UD = False if y2 <= q1 or q2 <= y1 else True

        return LR and UD

    # solution 2
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    #     return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]

    # solution 3
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    #     x1, y1, x2, y2 = rec1
    #     p1, q1, p2, q2 = rec2
    #     return (x2 - p1) * (x1 - p2) < 0 and (y2 - q1) * (y1 - q2) < 0


def test_solution():
    assert Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])
    assert not Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])
