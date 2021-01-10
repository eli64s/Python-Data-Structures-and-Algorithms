def plus_one(arr):
    """
    Time Complexity: O(n)
    Space Complexity: 
    """

    if not arr:
        return

    arr[-1] += 1

    for i in reversed(range(1, len(arr))):

        if arr[i] != 10:
            break

        arr[i] = 0
        arr[i - 1] += 1
    
    else:
        if arr[0] == 10:
            arr[0] = 1
            arr.append(0)

    return arr

print(plus_one([1,2,9]))
print(plus_one([9]))
print(plus_one([9,9,9]))
print(plus_one([]))