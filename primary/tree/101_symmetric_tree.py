# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        # solution 1
        # return root is None or self.R(root.left, root.right)

        # solution 2
        from collections import deque

        if not root:
            return True

        queue = deque([root, root])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False

            queue.extend([t1.left, t2.right])
            queue.extend([t1.right, t2.left])

        return True

    # def R(self, left: TreeNode, right: TreeNode):
    #     if not left or not right:
    #         return left == right
    #     if left.val != right.val:
    #         return False
    #     return self.R(left.right, right.left) and self.R(left.left, right.right)


def test_solution():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    assert Solution().isSymmetric(root1)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(3)
    root2.right.left = TreeNode(2)
    assert not Solution().isSymmetric(root2)
