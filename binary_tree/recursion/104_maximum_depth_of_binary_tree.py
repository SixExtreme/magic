# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    def maxDepth(self, root: TreeNode) -> int:
        from collections import deque

        if not root:
            return 0
        ans, queue = 0, deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans += 1
        return ans

    # solution 2
    # def maxDepth(self, root: TreeNode) -> int:
    #     return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test_solution():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    assert Solution().maxDepth(root) == 3


if __name__ == '__main__':
    test_solution()