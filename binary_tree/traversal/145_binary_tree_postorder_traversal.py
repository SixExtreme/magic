from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # solution 1
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans = []
    #     if root is None:
    #         return ans
    #     if root.left:
    #         ans.extend(self.postorderTraversal(root.left))
    #     if root.right:
    #         ans.extend(self.postorderTraversal(root.right))
    #     ans.append(root.val)
    #     return ans

    # solution 2
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     def LRM(_root: TreeNode, vals: List[int]):
    #         if not _root:
    #             return
    #         if _root.left:
    #             LRM(_root.left, vals)
    #         if _root.right:
    #             LRM(_root.right, vals)
    #         vals.append(_root.val)
    #
    #     ans = []
    #     if not root:
    #         return ans
    #     LRM(root, ans)
    #     return ans

    # solution 3
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     ans: List[int] = []
    #     if not root:
    #         return ans
    #     nstk: List[TreeNode] = []
    #     rstk: List[TreeNode] = []
    #     nstk.append(root)
    #     while nstk:
    #         node: TreeNode = nstk.pop()
    #         if node.left:
    #             nstk.append(node.left)
    #         if node.right:
    #             nstk.append(node.right)
    #         rstk.append(node)
    #     while rstk:
    #         ans.append(rstk.pop().val)
    #     return ans

    # solution 4
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans: List[int] = []
        if not root:
            return ans
        stack: List[TreeNode] = []
        curr: Optional[TreeNode] = root
        last: Optional[TreeNode] = None
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right and peek.right is not last:
                    curr = peek.right
                else:
                    last = stack.pop()
                    ans.append(last.val)
        return ans


def test_solution():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().postorderTraversal(root) == [3, 2, 1]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().postorderTraversal(root) == [4, 5, 2, 6, 7, 3, 1]


if __name__ == '__main__':
    test_solution()
