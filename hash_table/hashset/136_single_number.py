class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution 1
        # hset = set()
        # for x in nums:
        #     if x in hset:
        #         hset.remove(x)
        #     else:
        #         hset.add(x)
        # return hset.pop()

        # solution 2
        xor = 0
        for x in nums:
            xor ^= x
        return xor


def test_solution():
    nums = [1, 1, 2, 3, 3, 4, 4]
    assert Solution().singleNumber(nums) == 2
