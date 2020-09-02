import hashlib, datetime

class Block:

    def __init__(self, data, previous_hash=0):
      self.timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S %m/%d/%y ")
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

    def __repr__(self):
        s = '\nBlock('
        s += '\nTimestamp: {}'.format(self.timestamp)
        s += '\nData: {}'.format(self.data)
        s += '\nSHA256 Hash: {}'.format(self.hash)
        s += '\nPrevious Hash: {})'.format(self.previous_hash.hash if self.previous_hash else 0)
        return s


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def size(self):
        return self.length

    def append(self, value):
        if self.head == None:
            new_block = Block(value, None)
            self.head = new_block
            self.tail = self.head
        else:
            new_block = Block(value, self.tail)
            self.tail = new_block
        self.length += 1

    def __repr__(self):
        blocks = []
        next = self.tail

        while next:
            blocks.append(repr(next))
            next = next.previous_hash

        return "BlockChain({})".format(", ".join(blocks))

block_chain = BlockChain()
block_chain.append(None)
print(repr(block_chain))
block_chain.append(1)
block_chain.append("Some info")
block_chain.append(3)
print(repr(block_chain))
