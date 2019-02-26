class Solution:
    # solution 1
    # def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
    #     s = set()
    #     for i, x in enumerate(nums):
    #         if i > k:
    #             s.remove(nums[i - k - 1])
    #         if x not in s:
    #             s.add(x)
    #         else:
    #             return True
    #     return False

    # solution 2
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            s.add(x)
            if len(s) > k:
                s.remove(nums[i - k])
        return False


def test_solution():
    nums = [1, 2, 3, 1]
    assert Solution().containsNearbyDuplicate(nums, 3)

    nums = [1, 0, 1, 1]
    assert Solution().containsNearbyDuplicate(nums, 1)

    nums = [1, 2, 3, 1, 2, 3]
    assert not Solution().containsNearbyDuplicate(nums, 2)
