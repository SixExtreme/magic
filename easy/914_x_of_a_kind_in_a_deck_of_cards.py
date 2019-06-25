# from typing import List
#
#
# class Solution:
#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         hmap = dict()
#         for x in deck:
#             hmap[x] = hmap.get(x, 0) + 1
#         counts = set(hmap.values())
#         print(counts)
#         return len(counts) == 1 and counts.pop() >= 2
#
#
# def test_solution():
#     assert Solution().hasGroupsSizeX([1, 1, 2, 2, 2, 2])
#     assert Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])