from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans: List[int] = []
    #     if not root:
    #         return ans
    #     if root.left:
    #         ans.extend(self.inorderTraversal(root.left))
    #     ans.append(root.val)
    #     if root.right:
    #         ans.extend(self.inorderTraversal(root.right))
    #     return ans

    # solution 2
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     def LMR(_root: TreeNode, vals: List[int]):
    #         if not _root:
    #             return
    #         if _root.left:
    #             LMR(_root.left, vals)
    #         vals.append(_root.val)
    #         if _root.right:
    #             LMR(_root.right, vals)
    #
    #     ans: List[int] = []
    #     if not root:
    #         return ans
    #     LMR(root, ans)
    #     return ans

    # solution 3
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        pass


def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root) == [1, 3, 2]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().inorderTraversal(root) == [4, 2, 5, 1, 6, 3, 7]