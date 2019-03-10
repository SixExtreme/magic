class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int:
        ans, count = 0, 0
        for x in nums:
            if x == 0:
                count = 0
            else:
                count += x
            ans = max(ans, count)
        return ans


def test_solution():
    nums = [1, 1, 0, 1, 1, 1]
    assert Solution().findMaxConsecutiveOnes(nums) == 3
