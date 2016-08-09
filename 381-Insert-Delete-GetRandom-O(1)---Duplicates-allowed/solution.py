
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d = {}
        self._l = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val not in self._d
        self._l.append(val)
        loc = len(self._l)-1
        if ret:
            self._d[val] = [loc]
        else:
            self._d[val].append(loc)
        return ret

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self._d:
            return False
        locs = self._d[val]
        loc = locs[-1]
        del locs[-1]
        if not locs:
            del self._d[val]
        n = len(self._l)
        if loc>=n:
            return False
        if n-1==loc:
            del self._l[loc]
        else:
            last_v = self._l[-1]
            self._l[loc] = last_v
            self._d[last_v].append(loc)
            del self._l[-1]
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self._l)



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
