def dutch_flag_partition1(arr, pivot_idx):
    """ 
    Approach 1: Build three arrays - less, equal, greater.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    
    pivot = arr[pivot_idx]
    
    # First pass: group elements smaller than pivot
    for i in range(len(arr)):
        # Look for a smaller element
        for j in range(i + 1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
        
    # Second pass: group elements larger than pivot
    for i in reversed(range(len(arr))):
        # Look for a larger element
        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break 

    return arr


def dutch_flag_partition2(arr, pivot_idx):
    """ 
    Approach 2

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    pivot = arr[pivot_idx]
    
    smaller = 0

    # First pass: group elements smaller than pivot
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
        
    # Second pass: group elements larger than pivot
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1

    return arr


def dutch_flag_partition3(arr, pivot_idx):
    """ 
    Approach 3

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    pivot = arr[pivot_idx]
    smaller = 0
    equal = 0
    larger = len(arr)

    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]
    return arr

print(dutch_flag_partition1([0,1,2,0,2,1,1], 3))
print(dutch_flag_partition2([0,1,2,0,2,1,1], 3))
print(dutch_flag_partition3([0,1,2,0,2,1,1], 3))