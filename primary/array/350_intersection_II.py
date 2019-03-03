class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        # solution 1
        # ans = []
        #
        # m, n = len(nums1), len(nums2)
        # if m == 0 or n == 0:
        #     return ans
        #
        # more, less = nums1, nums2
        # if m < n:
        #     more, less = less, more
        #
        # counter = dict()
        # for x in more:
        #     counter[x] = counter.get(x, 0) + 1
        #
        # for x in less:
        #     if x in counter and counter[x] > 0:
        #         ans.append(x)
        #         counter[x] -= 1
        #
        # return ans

        # solution 2
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        return list((c1 & c2).elements())


def test_solution():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ans = Solution().intersect(nums1, nums2)

    counter = dict()
    for x in ans:
        counter[x] = counter.get(x, 0) + 1
    assert counter == {2: 2}
