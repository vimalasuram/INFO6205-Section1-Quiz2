import unittest
from BinarySearchRotated import binary_search_rotated

class TestBinarySearchRotated(unittest.TestCase):
    def test_found_in_first_half(self):
        arr = [4, 5, 6, 7, 0, 1, 2]
        rotation_index = 4
        self.assertTrue(binary_search_rotated(arr, 6, rotation_index))

    def test_found_in_second_half(self):
        arr = [4, 5, 6, 7, 0, 1, 2]
        rotation_index = 4
        self.assertTrue(binary_search_rotated(arr, 1, rotation_index))

    def test_not_found(self):
        arr = [4, 5, 6, 7, 0, 1, 2]
        rotation_index = 4
        self.assertFalse(binary_search_rotated(arr, 10, rotation_index))

    def test_single_element_not_found(self):
        arr = [5]
        rotation_index = 0
        self.assertFalse(binary_search_rotated(arr, 1, rotation_index))

    def test_empty_array(self):
        arr = []
        rotation_index = 0
        self.assertFalse(binary_search_rotated(arr, 3, rotation_index))

    def test_target_at_rotation_index(self):
        arr = [4, 5, 6, 7, 0, 1, 2]
        rotation_index = 4
        self.assertTrue(binary_search_rotated(arr, 0, rotation_index))

    def test_target_at_start_of_array(self):
        arr = [6, 7, 8, 1, 2, 3, 4, 5]
        rotation_index = 3
        self.assertTrue(binary_search_rotated(arr, 6, rotation_index))

    def test_target_at_end_of_array(self):
        arr = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
        rotation_index = 2
        self.assertTrue(binary_search_rotated(arr, 8, rotation_index))

    def test_large_array(self):
        arr = list(range(15, 100)) + list(range(0, 15))  # Rotated at index 85
        rotation_index = 85
        self.assertTrue(binary_search_rotated(arr, 14, rotation_index))
        self.assertTrue(binary_search_rotated(arr, 50, rotation_index))
        self.assertFalse(binary_search_rotated(arr, 200, rotation_index))

if __name__ == "__main__":
    unittest.main()