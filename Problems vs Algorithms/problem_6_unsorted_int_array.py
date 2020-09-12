def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)

    if n == 1:
        return (ints[0], ints[0])
    if n % 2 == 1:
        min = ints[0]
        max = ints[1]
        cur = 1
    else:
        if ints[0] < ints[1]:
            min = ints[0]
            max = ints[1]
        else:
            min = ints[1]
            max = ints[0]
        cur = 2

    while cur < n - 1:
        if ints[cur] < ints[cur + 1]:
            if ints[cur] < min:
                min = ints[cur]
            if ints[cur + 1] > max:
                max = ints[cur + 1]
        else:
            if ints[cur + 1] < min:
                min = ints[cur + 1]
            if ints[cur] > max:
                max = ints[cur]

        cur += 2
    return (min, max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 1) == get_min_max([1,1,1,1,1,1,0])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if ((-2, 10) == get_min_max([10,9,-2,1,2,3])) else "Fail")
