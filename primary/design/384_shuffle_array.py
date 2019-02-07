import copy
import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        # n = len(self.nums)
        # nums = copy.copy(self.nums)
        # for i in range(n):
        #     j = random.randint(0, n-1)
        #     nums[i], nums[j] = nums[j], nums[i]
        # return nums

        nums = copy.copy(self.nums)
        return random.sample(nums, len(self.nums))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()