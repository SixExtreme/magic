class Solution:
    def findKthLargest(self, nums: 'List[int]', k: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            divide = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[left]:
                    nums[i], nums[divide + 1] = nums[divide + 1], nums[i]
                    divide += 1
            nums[divide], nums[left] = nums[left], nums[divide]
            if divide == k - 1:
                return nums[divide]
            elif divide > k - 1:
                right = divide - 1
            elif divide < k - 1:
                left = divide + 1
        return nums[left]


def test_solution():
    nums, k = [3, 2, 1, 5, 6, 4], 2
    assert Solution().findKthLargest(nums, k) == 5

    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    assert Solution().findKthLargest(nums, k) == 4


if __name__ == '__main__':
    test_solution()
