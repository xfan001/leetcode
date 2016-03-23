import Queue

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        list = self.inorderTraversal(root)
        if len(list)%2 == 0:
            return False
        i, j = 0, len(list)-1
        while i<j:
            if (list[i] != list[j]):
                return False
            i += 1
            j -= 1
        return True

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = Queue.LifoQueue()
        ret_list = []
        while root or not stack.empty():
            while root:
                stack.put(root)
                root = root.left
            if not stack.empty():
                node = stack.get()
                ret_list.append(node.val)
                root = node.right
        return ret_list

if __name__ == '__main__':
    pass