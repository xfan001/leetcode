import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        i = 0
        p = head
        while p:
            i += 1
            p = p.next
        self.llen = i

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        num = random.randint(0, self.llen-1)
        i = 0
        p = self.head
        while i<num:
            i+=1
            p = p.next
        return p.val
            
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()