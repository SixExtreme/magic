# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     def symmetric(n1: TreeNode, n2: TreeNode):
    #         if not n1 and not n2:
    #             return True
    #         if not n1 or not n2:
    #             return False
    #         if n1.val != n2.val:
    #             return False
    #         return symmetric(n1.left, n2.right) and symmetric(n1.right, n2.left)
    #
    #     if not root:
    #         return True
    #     return symmetric(root.left, root.right)

    # solution 2
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque

        if not root:
            return True
        queue = deque([root.left, root.right])
        while queue:
            n1: TreeNode = queue.popleft()
            n2: TreeNode = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            queue.extend([n1.left, n2.right])
            queue.extend([n1.right, n2.left])
        return True


def test_solution():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    assert Solution().isSymmetric(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    assert not Solution().isSymmetric(root)