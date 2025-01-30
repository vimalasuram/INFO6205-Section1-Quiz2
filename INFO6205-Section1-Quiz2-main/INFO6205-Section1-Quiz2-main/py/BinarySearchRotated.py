def binary_search_rotated(arr, target, rotation_index):
    """
    Perform binary search on a rotated sorted array.
    
    :param arr: List[int] - The rotated sorted array.
    :param target: int - The number to search for.
    :param rotation_index: int - The index at which the array was rotated.
    :return: bool - True if the target is in the array, False otherwise.
    """
    
    # Helper function for standard binary search
    def binary_search(arr, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    # If rotation_index is 0, the array is not rotated, so we can perform normal binary search
    if rotation_index == 0:
        return binary_search(arr, 0, len(arr) - 1, target)
    
    # Check which half of the array to search in
    if target >= arr[rotation_index] and target <= arr[len(arr) - 1]:
        # Target is in the second half
        return binary_search(arr, rotation_index, len(arr) - 1, target)
    else:
        # Target is in the first half
        return binary_search(arr, 0, rotation_index - 1, target)
