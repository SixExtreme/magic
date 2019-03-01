class Solution:
    def minSubArrayLen(self, s: int, nums: 'List[int]') -> int:
        if len(nums) == 0:
            return 0
        _sum, _min = 0, 0

        i, j = 0, 0
        while j < len(nums):
            _sum += nums[j]
            j += 1

            while i < j and _sum >= s:
                _min = min(_min, j - i)
                _sum -= nums[i]
                i -= 1

        return _min


def test_solution():
    s, nums = 7, [2, 3, 1, 2, 4, 3]
    assert Solution().minSubArrayLen(s, nums) == 2
