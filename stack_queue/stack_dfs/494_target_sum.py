class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        return self.helper(nums, 0, 0, S, dict())

    def helper(self, nums, depth, acc, target, visit):
        key = '{}->{}'.format(depth, acc)
        if key in visit:
            return visit[key]

        if depth == len(nums):
            return 1 if acc == target else 0

        y = self.helper(nums, depth + 1, acc + nums[depth], target, visit)
        n = self.helper(nums, depth + 1, acc - nums[depth], target, visit)

        visit[key] = y + n
        return y + n


def test_solution():
    nums = [1, 1, 1, 1, 1]
    assert Solution().findTargetSumWays(nums, 3) == 5
