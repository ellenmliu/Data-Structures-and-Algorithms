Time Complexity: O(n) where n is the number of element
Space Complexity: O(1)

I chose to compare in pairs and iterate through the array once. This way it reduces the amount of comparisons. If we iterate, we do a total of 3 comparisons per 2 numbers, so our time complexity is around 3*n/2 depending on whether there are even or odd number of elements in the array. Which comes down to O(n) if we consider when n is really big number. I'm only storing max, min, and the current index, so space complexity is O(1).
