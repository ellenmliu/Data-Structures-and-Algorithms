def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or type(number) != int:
        return "Enter an int"
    if number == 0 or number == 1:
        return number
    start = 1
    end = number

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid > number:
            end = mid - 1
        elif mid * mid < number:
            start = mid + 1
            ans = mid

    return ans

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (4 == sqrt(24)) else "Fail")
print ("Pass" if  (100000000 == sqrt(10000000000000000)) else "Fail")
print ("Pass" if  ("Enter an int" == sqrt(None)) else "Fail")
print ("Pass" if  ("Enter an int" == sqrt("")) else "Fail")
