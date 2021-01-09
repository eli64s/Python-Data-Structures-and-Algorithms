# Binary Search 

def binary_search(sorted_list, target):
    """ 
    Time Complexity: O(log2(n))
    Space Complexity: O(1)
    """

    # Floor and ceiling indices are the "walls" that eclose the target value in the array   
    floor_idx = -1
    ceiling_idx = len(sorted_list)

    while (floor_idx + 1) < ceiling_idx:

        distance = ceiling_idx - floor_idx
        middle_idx = distance // 2
        guess_idx = floor_idx + middle_idx
        guess_value = sorted_list[guess_idx]

        # Target value is found
        if target == guess_value:
            print("Target number found in list at index {}".format(guess_idx))
            return True

        # Target value is to the left, update ceiling index 
        if guess_value > target:
            ceiling_idx = guess_idx

        # Target value is to the right, update floor index
        elif guess_value < target:
            floor_idx = guess_idx 

    return False


# Tests

import unittest

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = binary_search([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = binary_search([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = binary_search([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = binary_search([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = binary_search([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)
