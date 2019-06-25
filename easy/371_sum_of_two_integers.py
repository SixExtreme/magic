# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         if a == 0 or b == 0:
#             return a or b
#         while b != 0:
#             _xor = a ^ b
#             _and = a & b
#             a, b = _xor, _and << 1
#         return a
#
#
# def test_solution():
#     assert Solution().getSum(1, 2) == 3
#     assert Solution().getSum(-2, 3) == 1
