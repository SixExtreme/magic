class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        # i, j, k = m - 1, n - 1, len(nums1) - 1
        # while j >= 0:
        #     if i >= 0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     k -= 1

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
    nums1, m = [1, 2, 3, 0, 0, 0], 3
    nums2, n = [2, 5, 6], 3
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


if __name__ == '__main__':
    test_solution()
