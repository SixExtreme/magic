# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 2
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     if root.left and root.right:
    #         return 1 + min(
    #             self.minDepth(root.left),
    #             self.minDepth(root.right)
    #         )
    #     else:
    #         return 1 + self.minDepth(
    #             root.left or root.right
    #         )

    # solution 2
    def minDepth(self, root: TreeNode) -> int:
        from collections import deque

        if not root:
            return 0
        depth, queue = 1, deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not (node.left or node.right):
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth


def test_solution():
    root = TreeNode(1)
    assert Solution().minDepth(root) == 1

    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().minDepth(root) == 2

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().minDepth(root) == 3

    root.right.right = TreeNode(7)
    assert Solution().minDepth(root) == 3


if __name__ == '__main__':
    test_solution()
