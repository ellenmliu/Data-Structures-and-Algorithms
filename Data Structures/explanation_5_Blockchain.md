Time Complexity: O(1)
Space Complexity: O(n)

The only method that the block chain has is the append method, which takes O(1) time because we are storing the last inserted block. That way we don't have to iterate through the linked list every time we need to append. Space complexity would be O(n) to store all of the blocks in the block chain where n is the number of blocks.
