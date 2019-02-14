from collections import deque


class Solution:
    def openLock(self, deadends: 'List[str]', target: 'str') -> 'int':
        origin = '0000'
        deadends = set(deadends)

        if origin in deadends:
            return -1
        if origin == target:
            return 0

        ans, level = -1, 0
        visit, queue = {origin}, deque([origin])

        while queue:
            count = len(queue)

            for _ in range(count):
                node = queue.popleft()

                if node in deadends:
                    continue

                if node == target:
                    return level

                nums = list(node)
                for i in range(4):
                    temp = nums[i]

                    nums[i] = '9' if temp == '0' else chr(ord(temp) - 1)
                    node = ''.join(nums)
                    if node not in visit and node not in deadends:
                        visit.add(node)
                        queue.append(node)

                    nums[i] = '0' if temp == '9' else chr(ord(temp) + 1)
                    node = ''.join(nums)
                    if node not in visit and node not in deadends:
                        visit.add(node)
                        queue.append(node)

                    nums[i] = temp

            level += 1

        return ans


def test_solution():
    deadends, target = ['0000'], '8888'
    assert Solution().openLock(deadends, target) == -1

    deadends, target = ['8887', '8889', '8878', '8898', '8788', '8988', '7888', '9888'], '8888'
    assert Solution().openLock(deadends, target) == -1

    deadends, target = ['0201', '0101', '0102', '1212', '2002'], '0202'
    assert Solution().openLock(deadends, target) == 6


if __name__ == '__main__':
    test_solution()

