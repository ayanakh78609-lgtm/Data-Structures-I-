import time

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

for n in (10_000, 50_000, 100_000):
    data = list(range(n))  # Must be sorted.
    target = n - 1
    start = time.perf_counter()
    index = binary_search(data, target)
    elapsed = (time.perf_counter() - start) * 1_000_000
    print(f"Array size: {n:,} | Index: {index} | Time: {elapsed:.2f} microseconds")
