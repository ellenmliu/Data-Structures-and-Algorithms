import sys
class Node:
    def __init__(self, char=None, frequency=None, left=None, right=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right
        self.binary = ''

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def has_right(self):
        return self.right != None

    def has_left(self):
        return self.left != None

    def __repr__(self):
        return 'Node({}, {})'.format(self.char, self.frequency)

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.binary_codes = {}
        self.has_unique = False

    def get_root(self):
        return self.root

    def get_binary_codes(self, node):
        if node == self.root and not node.has_right() and not node.has_left():
            self.binary_codes[node.char] = '0'
            return self.binary_codes
        if node.has_left():
            node.get_left().binary = node.binary + '0'
            self.get_binary_codes(node.get_left())
        if node.has_right():
            node.get_right().binary = node.binary + '1'
            self.get_binary_codes(node.get_right())
        if node.char != None:
            self.binary_codes[node.char] = node.binary
        self.has_unique = True
        return self.binary_codes


class PriorityQueue:
    def __init__(self, initial_size=10):
        self.queue = []
        self.frontIndex = -1
        self.nextIndex = 0

    def enqueue(self, node):
        self.queue.append(node)
        self.queue = sorted(self.queue, key=lambda node: node.frequency)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def __repr__(self):
        nodes = []
        for i in self.queue:
            nodes.append(repr(i))

        return "PQ({})".format(", ".join(nodes))

def huffman_encoding(data):

    if data is None or data == '':
        print("Enter data to encode")
        return None, None

    frequency = {}

    for char in data:
        if char in frequency.keys():
            frequency[char] += 1
        else:
            frequency[char] = 1

    pq = PriorityQueue(len(frequency))

    for char in frequency.keys():
        pq.enqueue(Node(char, frequency[char]))

    while pq.size() > 1:
        first = pq.dequeue()
        second = pq.dequeue()
        new_node = Node(None, first.frequency + second.frequency, first, second)
        pq.enqueue(new_node)

    root = pq.dequeue()
    huffman_tree = Tree(root)
    binary_codes = huffman_tree.get_binary_codes(root)
    encoded = ''
    for char in data:
        encoded += binary_codes[char]
    return (encoded, huffman_tree)

def huffman_decoding(data, tree):
    decoded = ''
    current = tree.get_root()
    index = 0

    while index < len(data):
        if not tree.has_unique:
            decoded += current.char
        else:
            if data[index] == '0':
                current = current.get_left()
            if data[index] == '1':
                current = current.get_right()
            if not current.has_left() and not current.has_right():
                decoded += current.char
                current = tree.get_root()
        index += 1

    return decoded


if __name__ == "__main__":
    test_cases = ["The bird is the word", "AAAAAAABBBCCCCCCCDDEEEEEE", "", "A", "AAAAAA"]

    for a_great_sentence in test_cases:
        encoded_data, tree = huffman_encoding(a_great_sentence)

        if encoded_data:
            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))

            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))

        else:
            print("Entered data is empty")
