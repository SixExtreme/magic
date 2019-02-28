class Solution:
    def merge(self, nums1: 'List[int]', m: int, nums2: 'List[int]', n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1)
        while n > 0:
            if m > 0 and nums1[m - 1] > nums2[n - 1]:
                nums1[k - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[k - 1] = nums2[n - 1]
                n -= 1
            k -= 1


def test_solution():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    Solution().merge(nums1, 3, nums2, 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]
