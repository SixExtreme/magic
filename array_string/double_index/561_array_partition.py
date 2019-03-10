class Solution:
    def arrayPairSum(self, nums: 'List[int]') -> int:
        nums.sort()
        ans = 0
        for i in range(0, len(nums), 2):
            ans += nums[i]
        return ans


def test_solution():
    nums = [1, 4, 3, 2]
    assert Solution().arrayPairSum(nums) == 4
