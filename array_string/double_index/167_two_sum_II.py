class Solution:
    def twoSum(self, numbers: 'List[int]', target: int) -> 'List[int]':
        i, j = 0, len(numbers) - 1
        while i < j:
            _sum = numbers[i] + numbers[j]
            if _sum > target:
                j -= 1
            elif _sum < target:
                i += 1
            else:
                return [i + 1, j + 1]


def test_solution():
    numbers = [2, 7, 11, 15]
    assert Solution().twoSum(numbers, 9) == [1, 2]
