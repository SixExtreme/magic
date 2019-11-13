from typing import List


class Solution:
    @staticmethod
    def game(guess: List[int], answer: List[int]) -> int:
        # solution 1
        ans = 0
        for i in range(3):
            if guess[i] == answer[i]:
                ans += 1
        return ans

        # solution 2
        # ans = 0
        # if guess[0] == answer[0]:
        #     ans += 1
        # if guess[1] == answer[1]:
        #     ans += 1
        # if guess[2] == answer[2]:
        #     ans += 1
        # return ans


def test_solution():
    assert Solution().game([1, 2, 3], [1, 2, 3]) == 3
    assert Solution().game([2, 2, 3], [3, 2, 1]) == 1
