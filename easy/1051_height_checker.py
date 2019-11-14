from typing import List


class Solution:
    @staticmethod
    def heightChecker(heights: List[int]) -> int:
        # solution 1
        # ans = 0
        # for (i, x) in enumerate(sorted(heights)):
        #     if heights[i] != x:
        #         ans += 1
        # return ans

        # solution 2
        buckets: List[int] = [0] * 101
        for height in heights:
            buckets[height] += 1

        i, ans = 0, 0
        for height in range(1, 101):
            if buckets[height] == 0:
                continue
            for _ in range(buckets[height]):
                if heights[i] != height:
                    ans += 1
                i += 1
        return ans


def test_solution():
    assert Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3
