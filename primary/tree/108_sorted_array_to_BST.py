# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: 'List[int]') -> 'TreeNode':
        # solution 1
        # if not nums:
        #     return None
        # mid = len(nums) // 2
        # root = TreeNode(nums[mid])
        # if mid > 0:
        #     root.left = self.sortedArrayToBST(nums[:mid])
        # if mid + 1 < len(nums):
        #     root.right = self.sortedArrayToBST(nums[mid+1:])
        # return root

        # solution 2
        # def R(i: int, j: int) -> TreeNode:
        #     mid = (i + j) // 2
        #     root = TreeNode(nums[mid])
        #     if mid > i:
        #         root.left = R(i, mid - 1)
        #     if mid < j:
        #         root.right = R(mid + 1, j)
        #     return root
        #
        # if len(nums) == 0:
        #     return None
        # return R(0, len(nums) - 1)

        # solution 3
        if len(nums) == 0:
            return None

        root = TreeNode(0)
        i, j = 0, len(nums) - 1
        nstk, istk = [root], [i, j]
        while len(istk) != 0:
            node = nstk.pop()
            r, l = istk.pop(), istk.pop()

            mid = (l + r) // 2
            node.val = nums[mid]

            if mid > l:
                node.left = TreeNode(0)
                nstk.append(node.left)
                istk.extend([l, mid - 1])

            if mid < r:
                node.right = TreeNode(0)
                nstk.append(node.right)
                istk.extend([mid + 1, r])

        return root


def test_solution():
    def validate_BST(root):
        pre, stack = None, []
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre, root = root, root.right
        return True

    nums = [-10, -3, 0, 5, 9]
    assert validate_BST(Solution().sortedArrayToBST(nums))




