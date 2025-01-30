def binary_search_rotated(arr, target, rotation_index):
    """
    Perform binary search on a rotated sorted array.
    
    A rotated sorted array is an array that was initially sorted in ascending order
    but then rotated at a certain pivot index.
    
    Example:
    Original sorted array: [0, 1, 2, 4, 5, 6, 7]
    Rotated at index 4: [4, 5, 6, 7, 0, 1, 2]
    Here, the rotation index 4 means that the first four elements were moved to the end.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    
    # TODO: Check if the rotation_index is 0, meaning the array is not rotated.
    
    # TODO: Determine which half (before or after rotation_index) the target belongs to.
    
    def binary_search(arr, left, right, target):
        """
        Performs a binary search on a sorted array within the specified range.
        
        :param arr: List[int] - The sorted array to search in.
        :param left: int - The left boundary of the search range (inclusive).
        :param right: int - The right boundary of the search range (inclusive).
        :param target: int - The value to search for.
        :return: bool - True if the target is in the array, False otherwise.
        """
        # TODO: Implement standard binary search logic.
        
        return False
    
    # TODO: Perform binary search on the appropriate half using the nested function.
    
    return False  # TODO: Replace this with actual return value
