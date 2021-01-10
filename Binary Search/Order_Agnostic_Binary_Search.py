# Binary Search 

def binary_search(unsorted_list, target):
    """ 
    Time Complexity: O(log2(n))
    Space Complexity: O(1)
    """
    if not unsorted_list:
        return "Input array is empty."
        
    floor_idx = 0
    ceiling_idx = len(unsorted_list) - 1
    is_ascending = unsorted_list[floor_idx] < unsorted_list[ceiling_idx]

    while floor_idx <= ceiling_idx:

        guess_idx = floor_idx + (ceiling_idx - floor_idx) // 2
        guess_value = unsorted_list[guess_idx]

        if target == guess_value:
           return "Target number found in list at index {}".format(guess_idx)
           

        if is_ascending:
            if target < guess_value:
                ceiling_idx = guess_idx - 1
            else:
                floor_idx = guess_idx + 1
        
        else:
            if target > guess_value:
                ceiling_idx = guess_idx - 1
            else:
                floor_idx = guess_idx + 1

    return "Target number not found in list."


def main():
    print(binary_search([], 1))
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))
    print(binary_search([10, 6, 4], 11))
main()