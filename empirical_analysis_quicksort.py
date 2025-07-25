import time
import random
import numpy as np
import pandas as pd

# ------------------ Quicksort Implementations ------------------

def quicksort(arr):
    """Deterministic quicksort: uses middle element as pivot."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    """Randomized quicksort: uses random element as pivot."""
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# ------------------ Empirical Comparison ------------------

def compare_quicksort_performance():
    input_sizes = [100, 500, 1000, 2000]
    distributions = ['random', 'sorted', 'reversed']
    results = []

    for size in input_sizes:
        for dist in distributions:
            if dist == 'random':
                arr = np.random.randint(0, 10000, size=size).tolist()
            elif dist == 'sorted':
                arr = list(range(size))
            elif dist == 'reversed':
                arr = list(range(size, 0, -1))

            # Deterministic quicksort
            arr_copy = arr.copy()
            start = time.time()
            quicksort(arr_copy)
            det_time = time.time() - start

            # Randomized quicksort
            arr_copy = arr.copy()
            start = time.time()
            randomized_quicksort(arr_copy)
            rand_time = time.time() - start

            results.append({
                'Input Size': size,
                'Distribution': dist,
                'Deterministic Time (s)': round(det_time, 6),
                'Randomized Time (s)': round(rand_time, 6)
            })

    df = pd.DataFrame(results)
    print(df.to_string(index=False))

# ------------------ Run Comparison ------------------

if __name__ == "__main__":
    compare_quicksort_performance()
