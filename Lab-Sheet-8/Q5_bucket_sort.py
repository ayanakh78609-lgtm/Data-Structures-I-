def bucket_sort(values):
    if not values: return []
    low, high = min(values), max(values)
    if low == high: return values.copy()
    buckets = [[] for _ in range(len(values))]
    for value in values:
        index = min(int((value - low) / (high - low) * (len(values) - 1)), len(values) - 1)
        buckets[index].append(value)
    result = []
    for bucket in buckets: result.extend(sorted(bucket))
    return result
values = [42, 32, 23, 52, 25, 47, 51]
print("Before sorting:", values); print("After bucket sort:", bucket_sort(values))
