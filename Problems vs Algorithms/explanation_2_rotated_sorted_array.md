Time Complexity: O(log(n))
Space Complexity: O(1)

For this problem, in order to stay within O(log(n)) time complexity, I decided to implement similar to a binary search. However this time it's modified in a way where we checked whether or not if the either half is sorted. To do this we compare whether the start index is smaller than the mid or if the end index is bigger than the mid. Once we know which half is sorted, we can check if the target number is within the sorted half by comparing to the boundaries and we would do a binary search within that sorted array recursively. Space complexity is O(1) because I'm not storing anything other than mid as an int.
