class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        if len(nums) == 0:
            return

        m = dict()
        for i, x in enumerate(nums):
            if x in m:
                return [m[x] ,i]
            else:
                m[target - x] = i
        return


def test_solution():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
