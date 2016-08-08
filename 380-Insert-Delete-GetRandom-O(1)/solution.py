import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.l = list()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.l.append(val)
        self.d[val] = len(self.l)-1
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        index = self.d[val]
        n  = len(self.l)
        self.l[index] = self.l[n-1]
        self.d[self.l[index]] = index
        del self.d[val]
        del self.l[-1]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()