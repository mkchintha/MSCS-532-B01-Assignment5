def quicksort(arr):
    """
    Deterministic Quicksort implementation.
    - Selects the middle element as the pivot.
    - Recursively sorts left and right subarrays.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Select middle element as pivot
    left = [x for x in arr if x < pivot]       # Elements less than pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to pivot
    right = [x for x in arr if x > pivot]      # Elements greater than pivot
    return quicksort(left) + middle + quicksort(right)