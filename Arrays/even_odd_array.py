def even_odd(arr):
    """ 
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    next_even = 0
    next_odd = len(arr) - 1

    while next_even < next_odd:

        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
    
    return arr

print(even_odd([2,1,4]))