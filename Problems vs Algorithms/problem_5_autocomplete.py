# from ipywidgets import widgets
# from IPython.display import display
# from ipywidgets import interact

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = {}

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        result = list()
        def traverse(node, cur_suffix):
            if node.is_word:
                result.append(cur_suffix)
            for char in node.children:
                new_suffix = cur_suffix + char
                traverse(node.children[char], new_suffix)
        traverse(self, '')
        return result


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        if type(prefix) != str:
            return "Enter a string"
        current = self.root

        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        return current

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


prefixNode = MyTrie.find("ant")
print('\n'.join(prefixNode.suffixes()))
prefixNode = MyTrie.find("f")
print('\n'.join(prefixNode.suffixes()))
prefixNode = MyTrie.find("t")
print('\n'.join(prefixNode.suffixes()))
prefixNode = MyTrie.find("")
print('\n'.join(prefixNode.suffixes()))
prefixNode = MyTrie.find(None)
print(prefixNode)

# def f(prefix):
#     if prefix != '':
#         prefixNode = MyTrie.find(prefix)
#         if prefixNode:
#             print('\n'.join(prefixNode.suffixes()))
#         else:
#             print(prefix + " not found")
#     else:
#         print('')
# interact(f,prefix='');
