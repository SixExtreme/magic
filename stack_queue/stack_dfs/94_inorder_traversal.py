# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # solution 1
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     ans = []
    #     self.inorder(root, ans)
    #     return ans
    #
    # def inorder(self, root, ans):
    #     if not root:
    #         return
    #     if root.left:
    #         self.inorder(root.left, ans)
    #     ans.append(root.val)
    #     if root.right:
    #         self.inorder(root.right, ans)

    # solution 2
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     ans = []
    #
    #     if not root:
    #         return ans
    #
    #     if root.left:
    #         ans.extend(self.inorderTraversal(root.left))
    #     ans.append(root.val)
    #     if root.right:
    #         ans.extend(self.inorderTraversal(root.right))
    #
    #     return ans

    # solution 3
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        if not root:
            return ans

        stack = []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return ans
            root = stack.pop()
            ans.append(root.val)
            root = root.right

        return ans


def test_solution():
    import sys
    sys.setrecursionlimit(10000)

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root) == [1, 3, 2]
