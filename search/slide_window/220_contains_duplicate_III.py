class Solution:
    # solution 1
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: 'int', t: 'int') -> 'bool':
        if t < 0:
            return False
        _map = dict()
        for i, x in enumerate(nums):
            m = x // (t + 1)
            if m in _map:
                return True
            if m - 1 in _map and abs(nums[i] - _map[m - 1]) <= t:
                return True
            if m + 1 in _map and abs(nums[i] - _map[m + 1]) <= t:
                return True
            _map[m] = x
            if i >= k:
                del _map[nums[i - k] // (t + 1)]
            print(x, m, _map)
        return False

    # solution 2
    # def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: 'int', t: 'int') -> 'bool':
    #     n = len(nums)
    #     if n <= 1:
    #         return False
    #
    #     s = set()
    #
    #     for i, x in enumerate(nums):
    #         if t == 0:
    #             if x in s:
    #                 return True
    #         else:
    #             for y in s:
    #                 if abs(nums[i] - y) <= t:
    #                     return True
    #
    #         s.add(nums[i])
    #         if len(s) > k:
    #             s.remove(nums[i - k])
    #
    #     return False


def test_solution():
    nums = [3, 2, 1]
    assert Solution().containsNearbyAlmostDuplicate(nums, 1, 1)

    nums = [1, 2, 3, 1]
    assert Solution().containsNearbyAlmostDuplicate(nums, 3, 0)

    nums = [1, 0, 1, 1]
    assert Solution().containsNearbyAlmostDuplicate(nums, 1, 2)

    nums = [1, 5, 8, 1, 5, 8]
    assert Solution().containsNearbyAlmostDuplicate(nums, 2, 3)


if __name__ == '__main__':
    test_solution()
