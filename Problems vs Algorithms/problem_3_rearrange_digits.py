def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    sorted = mergeSort(input_list)
    return combine(sorted)

def mergeSort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    right = input_list[:mid]
    left = input_list[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    right_ind = 0
    left_ind = 0

    while right_ind < len(right) and left_ind < len(left):
        if left[left_ind] > right[right_ind]:
            merged.append(left[left_ind])
            left_ind += 1
        else:
            merged.append(right[right_ind])
            right_ind += 1

    merged += left[left_ind:]
    merged += right[right_ind:]

    return merged

def combine(sorted):
    twoNum = [0, 0]
    for i, v in enumerate(sorted):
        twoNum[i%2] = twoNum[i%2] * 10 + v
    return twoNum

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 0], [0, 0]])
test_function([[1, 1, 1, 1, 1, 1], [111, 111]])
