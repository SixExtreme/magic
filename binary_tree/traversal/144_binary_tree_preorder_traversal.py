from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def MLR(root: TreeNode, vals: List[int]):
            if not root:
                return
            vals.append(root.val)
            if root.left:
                MLR(root.left, vals)
            if root.right:
                MLR(root.right, vals)

        ans = []
        if not root:
            return ans
        MLR(root, ans)
        return ans

    # solution 2
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     ans.append(root.val)
    #     if root.left:
    #         ans.extend(self.preorderTraversal(root.left))
    #     if root.right:
    #         ans.extend(self.preorderTraversal(root.right))
    #     return ans

    # solution 3
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     stack = [root]
    #     while stack:
    #         node = stack.pop()
    #         ans.append(node.val)
    #         if node.right:
    #             stack.append(node.right)
    #         if node.left:
    #             stack.append(node.left)
    #     return ans

    # solution 4
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     stack = []
    #     while root:
    #         ans.append(root.val)
    #         if root.right:
    #             stack.append(root.right)
    #         root = root.left
    #         if stack and not root:
    #             root = stack.pop()
    #     return ans

    # solution 5
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     curr = root
    #     while curr:
    #         if not curr.left:
    #             ans.append(curr.val)
    #             curr = curr.right
    #         else:
    #             most_right = curr.left
    #             while most_right.right and curr is not most_right.right:
    #                 most_right = most_right.right
    #             if most_right.right:
    #                 curr = curr.right
    #                 most_right.right = None
    #             else:
    #                 # 落叶归根之前
    #                 ans.append(curr.val)
    #                 most_right.right = curr
    #                 curr = curr.left
    #     return ans


def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().preorderTraversal(root) == [1, 2, 3]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().preorderTraversal(root) == [1, 2, 4, 5, 3, 6, 7]

