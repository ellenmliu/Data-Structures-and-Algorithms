import hashlib, datetime

class Block:

    def __init__(self, data, previous_hash=0):
      self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m/%d/%y ")
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
      sha = hashlib.sha256()

      hash_str = data.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
        s = '\nBlock('
        s += '\nTimestamp: {}'.format(self.timestamp)
        s += '\nData: {}'.format(self.data)
        s += '\nSHA256 Hash: {}'.format(self.hash)
        s += '\nPrevious Hash: {})'.format(self.previous_hash)
        return s


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return self.length

    def append(self, value):
        if value == None or type(value) is not str:
            print("Please enter a string value")
            return
        if self.head == None:
            new_block = Block(value, None)
            self.head = new_block
            self.tail = self.head
        else:
            new_block = Block(value, self.tail.hash)
            self.tail.next = new_block
            self.tail = self.tail.next
        self.length += 1

    def __repr__(self):
        blocks = []
        next = self.head

        while next:
            blocks.append(repr(next))
            next = next.next

        return "BlockChain({})".format(", ".join(blocks))

block_chain = BlockChain()
print(repr(block_chain))
block_chain.append("1")
block_chain.append("Some info")
block_chain.append("1 Some more testing")
print(repr(block_chain))

# Edge test cases
block_chain.append("")
print(repr(block_chain))
block_chain.append(None)
block_chain.append(123)
print(repr(block_chain))
