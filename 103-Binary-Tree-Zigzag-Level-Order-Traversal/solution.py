# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        num_of_floor = 0
        ret_list = []
        current_floor = None
        if root:
            current_floor = [root]
            ret_list.append([root.val])
        while current_floor:
            last_floor, current_floor = current_floor, []
            num_of_floor += 1
            vals = []
            for node in last_floor[::-1]:
                if num_of_floor%2:
                    first_node, second_node = node.right, node.left
                else:
                    first_node, second_node = node.left, node.right
                if first_node:
                    current_floor.append(first_node)
                    vals.append(first_node.val)
                if second_node:
                    current_floor.append(second_node)
                    vals.append(second_node.val)
            if vals:
                ret_list.append(vals)
        return ret_list

