import random
def randomized_quicksort(arr):
    """
    Randomized Quicksort implementation.
    - Selects a random pivot from the array.
    - Recursively sorts left and right subarrays.
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot selection
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)