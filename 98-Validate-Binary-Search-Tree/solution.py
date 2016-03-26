# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        from sys import maxint
        return self.isValid(root, -maxint-1, maxint)

    def isValid(self, root, lmin, rmax):
        if not root:
            return True
        if root.val >= rmax or root.val <= lmin:
            return False
        return self.isValid(root.left, lmin, root.val) and self.isValid(root.right, root.val, rmax)
        