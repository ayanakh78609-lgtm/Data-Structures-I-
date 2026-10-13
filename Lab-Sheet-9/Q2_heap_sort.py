def heap_sort(values):
    a = values.copy(); n = len(a)
    def sift_down(end, root):
        while 2*root+1 < end:
            child = 2*root+1
            if child+1 < end and a[child] < a[child+1]: child += 1
            if a[root] >= a[child]: return
            a[root], a[child] = a[child], a[root]; root = child
    for root in range(n//2-1, -1, -1): sift_down(n, root)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]; sift_down(end, 0)
    return a
values = [40, 10, 30, 50, 20]
print("Before sorting:", values); print("After heap sort:", heap_sort(values))
