Time Complexity: O(m + n)
Space Complexity: O(m + n)

In order to store either the union and intersection, we would have to go through each linked list once each, which gives up O(m + n) where m is length of linked list 1 and n is length of linked list 2. To store what values once we have visited the values, I chose to use a set, which is a hash map, to eliminate duplicates and also to ensure O(1) when checking if the value is present in the first linked list. That way the time complexity is still at O(m + n).
