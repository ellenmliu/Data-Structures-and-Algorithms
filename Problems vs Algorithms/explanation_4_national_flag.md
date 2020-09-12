Time Complexity: O(n) where n is the number of elements
Space Complexity: O(1)

I iterate through the array once, using markers of where 0s end and 2s start. That way if I encounter either number, then it would swap with whichever number was at that location. This way it would traverse through the array once and it would only take O(n) time. Space complexity would be constant time, O(1), because I'm only storing the indices of start, end, and current.
