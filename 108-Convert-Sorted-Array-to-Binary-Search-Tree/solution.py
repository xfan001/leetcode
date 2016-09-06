# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sort(nums, 0, len(nums)-1)
    
    def sort(self, nums, start, end):
        if start > end:
            return None
        mid = (start + end) / 2
        node = TreeNode(nums[mid])
        if start == end:
            return node
        node.left = self.sort(nums, start, mid-1)
        node.right = self.sort(nums, mid+1, end)
        return node