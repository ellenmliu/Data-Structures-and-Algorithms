RouteTrieNode Insert
Time Complexity: O(1)
Space Complexity: O(1)

We are only adding a TrieNode to the children list of the current node, which is a dictionary and so it takes O(1) to insert and takes O(1) to store.
--------------------------------------------------------------------------------
RouteTrie Insert
Time Complexity: O(n) where n is the number of directories in the path
Space Complexity: O(n) where n is the number of directories in the path

To insert, we have to iterate through each directory of the path after split and store that as a TrieNode each as the previous directory's children. That gives us the time and space complexity of O(n).
--------------------------------------------------------------------------------
RouteTrie Find Handler
Time Complexity: O(n) where n is the number of directories in the path
Space Complexity: O(1)

To find the node, we have to check through if the current directory is in the children, which is a list. We don't have to iterate through each level, which is usually different from the autocomplete Find method. That gives us time complexity of O(n) where n is the number of directories/folders in the path. Storage is O(1) because we are only storing the current node that we are on.
--------------------------------------------------------------------------------
Router Add Handler
Time Complexity: O(n) where n is the number of directories in the path
Space Complexity: O(1)

This is just the wrapper for RouteTrie insert so it will have the same time and space complexity
--------------------------------------------------------------------------------
Router Lookup
Time Complexity: O(n) where n is the number of directories in the path
Space Complexity: O(n) where n is the number of directories in the path

This is essentially a wrapper for RouteTrie find. We are returning the root handler which is constant and if there's isn't a handler found, we return not found, which is constant. So it will have the same time complexity as RouteTrie find. For storage, we do store the paths to be passed into find function so that gives us O(n) space complexity.
--------------------------------------------------------------------------------
Router Split Path
Time Complexity: O(n) where n is the number of chars in the path
Space Complexity: O(m) where n is the number of directories in the path

The split function is O(n) time complexity and O(m) for storage because we need to store the amount of directories within the path after it's split from the / separator.
