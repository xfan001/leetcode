import Queue
class Solution(object):
    def inorderTraversal(self, root):
        stack = Queue.LifoQueue()
        ret_list = []
        stack.put((root, False))
        while not stack.empty():
            root, isvisited = stack.get()
            if not root:
                continue
            if isvisited:
                ret_list.append(root.val)
            else:
                stack.put((root.right, False))
                stack.put((root, True))
                stack.put((root.left, False))
        return ret_list
        