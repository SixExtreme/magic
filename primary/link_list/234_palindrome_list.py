# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        if len(nums) == 0 or len(nums) == 1:
            return True
