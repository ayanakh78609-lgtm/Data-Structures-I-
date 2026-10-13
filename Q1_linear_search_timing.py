import time

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

for n in (10_000, 50_000, 100_000):
    data = list(range(n))
    target = n - 1  # Worst case: target is at the end.
    start = time.perf_counter()
    index = linear_search(data, target)
    elapsed = (time.perf_counter() - start) * 1_000_000
    print(f"Array size: {n:,} | Index: {index} | Time: {elapsed:.2f} microseconds")
