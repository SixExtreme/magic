class Solution:
    def fourSum(self, nums: 'List[int]', target: 'int') -> 'List[List[int]]':
        ans = []

        n = len(nums)
        if n < 4:
            return ans

        nums.sort()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        ans.append((nums[i], nums[j], nums[l], nums[r]))
                        while l < r:
                            l += 1
                            if nums[l] != nums[l - 1]: break
                        while l < r:
                            r -= 1
                            if nums[r] != nums[r + 1]: break

        return ans


def test_solution():
    nums = [1, 0, -1, 0, -2, 2]
    res = {
        (-1, 0, 0, 1),
        (-2, -1, 1, 2),
        (-2, 0, 0, 2)
    }
    assert set(Solution().fourSum(nums, 0)) == res
