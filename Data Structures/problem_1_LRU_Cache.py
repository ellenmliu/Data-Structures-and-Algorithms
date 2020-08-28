class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return str(self.key)

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return self.length

    def enqueue(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = self.tail.next
        self.length += 1

    def dequeue(self):
        if self.size() == 0:
            return None
        head_key = self.head.key
        self.head = self.head.next
        self.head.previous = None
        self.length -= 1
        return head_key

    def remove(self, node):
        previous_node = node.previous
        next_node = node.next

        if self.head == node:
            self.head = next_node
        elif self.tail == node:
            self.tail = previous_node
        else:
            previous_node.next = next_node
            next_node.previous = previous_node

        node.next = None
        node.previous = None
        self.length -= 1

    def __repr__(self):
        lst = []
        node = self.head

        while node is not None:
            lst.append(repr(node))
            node = node.next
        return "Queue({})".format(", ".join(lst))


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.order = Queue()
        self.cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            node = self.cache[key]
            self.order.remove(node)
            self.order.enqueue(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key not in self.cache:
            if self.order.size() >= self.capacity:
                oldest = self.order.dequeue()
                if oldest:
                    del self.cache[oldest]
                else:
                    return
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.order.enqueue(new_node)

    def __repr__(self):
        s = ""
        for key in self.cache:
            s += str(key) + " Node(" + str(self.cache[key].key) + ", " + str(self.cache[key].value) + "), "
        return s

def original_test_case():
    print("Original Test Case")
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    actual = our_cache.get(1)
    print("Get 1: {} ".format(actual), "pass" if actual == 1 else "fail")
    actual = our_cache.get(2)
    print("Get 2: {} ".format(actual), "pass" if actual == 2 else "fail")
    actual = our_cache.get(9)
    print("Get 9: {} ".format(actual), "pass" if actual == -1 else "fail")
    our_cache.set(5, 5)
    our_cache.set(6, 6)

    actual = our_cache.get(3)
    print("Get 3: {} ".format(actual), "pass" if actual == -1 else "fail")

def size_zero_test_case():
    print("\nSize Zero Test Case")
    our_cache = LRU_Cache(0)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    actual = our_cache.get(1)
    print("Get 1: {} ".format(actual), "pass" if actual == -1 else "fail")
    actual = our_cache.get(2)
    print("Get 2: {} ".format(actual), "pass" if actual == -1 else "fail")

def bigger_test_case():
    print("\nBigger Test Case")
    our_cache = LRU_Cache(10)

    our_cache.set(10, 1);

    actual = our_cache.get(10)
    print("Get 10: {} ".format(actual), "pass" if actual == 1 else "fail")

    our_cache.set(22, 2);
    our_cache.set(33, 3);
    our_cache.set(44, 4);
    our_cache.set(555555, 5);

    actual = our_cache.get(1)
    print("Get 1: {} ".format(actual), "pass" if actual == -1 else "fail")

    our_cache.set(11, 1);
    our_cache.set(20, 2);
    our_cache.set(30, 3);
    our_cache.set(40, 4);
    our_cache.set(55, 5);
    our_cache.set(6, 6);

    actual = our_cache.get(10)
    print("Get 10: {} ".format(actual), "pass" if actual == -1 else "fail")
    actual = our_cache.get(555555)
    print("Get 555555: {} ".format(actual), "pass" if actual == 5 else "fail")
    actual = our_cache.get(33)
    print("Get 33: {} ".format(actual), "pass" if actual == 3 else "fail")


original_test_case()
size_zero_test_case()
bigger_test_case()
