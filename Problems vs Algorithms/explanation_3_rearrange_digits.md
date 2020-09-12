Time Complexity: O(n log(n)) where n is the number of elements
Space Complexity: O(n) where n is the number of elements

For this problem, I approached it with a merge sort to get the array of digits to be sorted by descending order. Using a merge sort gives a time complexity of O(n log(n)). Then when we go through the sorted array, we can assign the digits by assigning the biggest number first and each digit will be placed at the end of the number, which takes O(n) time. For storage, we need only maximum the amount of elements in the input element, O(n). We are assuming that every time we merge, we get rid of the arrays that we created.
