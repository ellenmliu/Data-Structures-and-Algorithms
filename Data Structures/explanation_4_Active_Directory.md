Time Complexity: O(mn)
Space Complexity: O(mn)

We would have to start at the current group and check if the user is in users list. If not, we would recurse into each the sub groups and keep checking if the user exists within the sub group. That would give us the time complexity similar to problem 2 which is O(mn) where m is the amount of sub groups and n is the number of users. Similarly, the space complexity will also be O(mn) because of the about of sub groups within a directory and n is the number of users.
