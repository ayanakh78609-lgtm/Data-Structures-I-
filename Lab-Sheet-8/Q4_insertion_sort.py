def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key, j = a[i], i - 1
        while j >= 0 and a[j] > key: a[j + 1] = a[j]; j -= 1
        a[j + 1] = key
    return a
values = [12, 11, 13, 5, 6]
print("Before sorting:", values); print("After insertion sort:", insertion_sort(values))
