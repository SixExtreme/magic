class Solution:
    def maxArea(self, heights: 'List[int]') -> int:
        max_area = 0
        i, j = 0, len(heights) - 1
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area


def test_solution():
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert Solution().maxArea(heights) == 49
