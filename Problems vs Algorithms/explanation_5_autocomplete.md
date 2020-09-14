TrieNode Insert
Time Complexity: O(1)
Space Complexity: O(1)

We are only adding a TrieNode to the children list of the current node, which is a dictionary and so it takes O(1) to insert and takes O(1) to store.
--------------------------------------------------------------------------------
TrieNode Find Suffixes
Time Complexity: O(m * n) where m is how many elements within a level and n is the depth of the level
Space Complexity: O(m * n) where m is how many elements within a level and n is the depth of the level

Since we are going through and find all the suffixes that the prefix has, we would have to go through each children key that the current prefix has and traverse through each level until we reached the end of the word. That gives us O(m*n) time and space.
--------------------------------------------------------------------------------
Trie Insert
Time Complexity: O(n) where n is the number of chars in the word
Space Complexity: O(n) where n is the number of chars in the word

To insert, we have to iterate through each letter of the word and store that as a TrieNode each as the previous letter's children. That gives us the time and space complexity of O(n).
--------------------------------------------------------------------------------
Trie Find Prefix Node
Time Complexity: O(n) where n is the number of chars in the word
Space Complexity: O(1)

To find the prefix node, we have to iterate through each letter of the input and check if its in the Trie. That gives us time complexity of O(n). Storage is O(1) because we are only storing the current node that we are on.
