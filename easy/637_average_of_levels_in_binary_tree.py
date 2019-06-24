from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque

        ans = []
        if not root:
            return ans

        queue = deque([root])
        while queue:
            size, _sum, _cnt = len(queue), 0, 0
            for _ in range(size):
                node = queue.popleft()
                _cnt += 1
                _sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(_sum / _cnt)

        return ans


def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert Solution().averageOfLevels(root) == [3, 14.5, 11]