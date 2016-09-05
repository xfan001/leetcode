
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None
        self.pre = None


class DLinkList(object):
    def __init__(self, maxlen):
        self.tail = None
        self.head = None
        self.maxlen = maxlen
        self.count = 0

    def pushHead(self, node):
        if self.isEmpty():
            node.pre = None
            node.next = None
            self.head = node
            self.tail = node
        else:
            node.pre = None
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.count += 1

    def removeNode(self, node):
        preNode = node.pre
        nextNode = node.next
        if preNode and nextNode:
            preNode.next = nextNode
            nextNode.pre = preNode
        elif not preNode and nextNode:
            nextNode.pre = None
            self.head = nextNode
        elif not nextNode and preNode:
            preNode.next = None
            self.tail = preNode
        else:
            self.head, self.tail = None, None
        self.count -= 1

    def isFull(self):
        return self.count == self.maxlen

    def isEmpty(self):
        return self.count == 0

    def __str__(self):
        node = self.head
        ks = []
        while node:
            ks.append(str(node.k))
            node = node.next
        return ','.join(ks)


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.kvs = {}
        self.cache = DLinkList(capacity)

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.kvs:
            node = self.kvs[key]
            self.cache.removeNode(node)
            self.cache.pushHead(node)
            return node.v
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.kvs:
            node = self.kvs[key]
            node.v = value
            self.cache.removeNode(node)
            self.cache.pushHead(node)
        else:
            newNode = Node(key, value)
            self.kvs[key] = newNode
            if not self.cache.isFull():
                self.cache.pushHead(newNode)
            else:
                tailNode = self.cache.tail
                del self.kvs[tailNode.k]
                self.cache.removeNode(tailNode)
                self.cache.pushHead(newNode)