# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        cur_list = [(root, root.val)]
        while True:
            last_list, cur_list = cur_list, []
            is_bottom = True
            for node, v in last_list:
                if not node.left and not node.right:
                    cur_list.append((node, v))
                    continue
                if node.left:
                    is_bottom = False
                    cur_list.append((node.left, v*10+node.left.val))
                if node.right:
                    is_bottom = False
                    cur_list.append((node.right, v*10+node.right.val))
            if is_bottom:
                break
        return sum([v for n,v in cur_list])