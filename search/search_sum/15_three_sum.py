class Solution:
    # solution 1
    # def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
    #     ans = set()
    #     for i, x in enumerate(nums):
    #         m, target = dict(), -x
    #         for j, y in enumerate(nums):
    #             if i == j:
    #                 continue
    #             if y not in m:
    #                 m[target - y] = j
    #             else:
    #                 z = nums[m[y]]
    #                 if (x, y, z) in ans:
    #                     continue
    #                 if (x, z, y) in ans:
    #                     continue
    #                 if (y, x, z) in ans:
    #                     continue
    #                 if (y, z, x) in ans:
    #                     continue
    #                 if (z, x, y) in ans:
    #                     continue
    #                 if (z, y, x) in ans:
    #                     continue
    #                 ans.add((x, y, z))
    #     return list(ans)

    # solution 2
    # def threeSum(self, nums):
    #     ans = []
    #
    #     if len(nums) < 3:
    #         return ans
    #
    #     nums.sort()
    #     for i in range(len(nums) - 2):
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         l, r = i + 1, len(nums) - 1
    #         while l < r:
    #             s = nums[i] + nums[l] + nums[r]
    #             if s < 0:
    #                 l += 1
    #             elif s > 0:
    #                 r -= 1
    #             else:
    #                 ans.append((nums[i], nums[l], nums[r]))
    #                 while l < r:
    #                     l += 1
    #                     if nums[l] != nums[l - 1]: break
    #                 while l < r:
    #                     r -= 1
    #                     if nums[r] != nums[r + 1]: break
    #
    #     return ans

    # solution 3
    def threeSum(self, nums):
        n, ans = len(nums), set()
        if n < 3:
            return ans

        def two_sum(nums, l, r, target):
            k = r - l + 1
            if k < 2:
                return

            ret = set()
            m, x = dict(), nums[l - 1]
            for i in range(l, r + 1):
                if nums[i] not in m:
                    m[target - nums[i]] = i
                else:
                    z = nums[i]
                    y = nums[m[z]]
                    ret.add((x, y, z))
            return ret

        nums.sort()
        for i, x in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ans |= two_sum(nums, i + 1, len(nums) - 1, -nums[i])
        return list(ans)


def test_solution():
    nums = [-1, 0, 1, 2, -1, -4]
    assert set(Solution().threeSum(nums)) == {(-1, 0, 1), (-1, -1, 2)}
