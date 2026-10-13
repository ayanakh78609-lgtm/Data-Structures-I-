import time

def linear_search(a, x):
    for i, v in enumerate(a):
        if v == x: return i
    return -1
def binary_search(a, x):
    low, high = 0, len(a)-1
    while low <= high:
        mid = (low+high)//2
        if a[mid] == x: return mid
        if a[mid] < x: low = mid+1
        else: high = mid-1
    return -1
def bubble_sort(a):
    a=a.copy()
    for i in range(len(a)):
        changed=False
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]; changed=True
        if not changed: break
    return a
def selection_sort(a):
    a=a.copy()
    for i in range(len(a)):
        m=i
        for j in range(i+1,len(a)):
            if a[j]<a[m]: m=j
        a[i],a[m]=a[m],a[i]
    return a
def insertion_sort(a):
    a=a.copy()
    for i in range(1,len(a)):
        key=a[i]; j=i-1
        while j>=0 and a[j]>key: a[j+1]=a[j]; j-=1
        a[j+1]=key
    return a
def quick_sort(a):
    if len(a)<=1:return a
    pivot=a[len(a)//2]
    return quick_sort([x for x in a if x<pivot])+[x for x in a if x==pivot]+quick_sort([x for x in a if x>pivot])
def merge_sort(a):
    if len(a)<=1:return a
    mid=len(a)//2; left=merge_sort(a[:mid]); right=merge_sort(a[mid:]); out=[]; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: out.append(left[i]); i+=1
        else: out.append(right[j]); j+=1
    return out+left[i:]+right[j:]
def bucket_sort(a):
    if not a:return []
    lo,hi=min(a),max(a)
    if lo==hi:return a.copy()
    buckets=[[] for _ in a]
    for x in a:
        idx=min(int((x-lo)/(hi-lo)*(len(a)-1)),len(a)-1); buckets[idx].append(x)
    out=[]
    for b in buckets: out.extend(sorted(b))
    return out

if __name__ == "__main__":
    data = [64, 25, 12, 22, 11, 90, 34, 7, 51, 19]
    print("Identical input data:", data)
    for name, fn in [("Bubble",bubble_sort),("Selection",selection_sort),("Insertion",insertion_sort),("Quick",quick_sort),("Merge",merge_sort),("Bucket",bucket_sort)]:
        start=time.perf_counter(); result=fn(data); elapsed=(time.perf_counter()-start)*1_000_000
        print(f"{name} sort: {result} | {elapsed:.2f} microseconds")
    sorted_data=sorted(data); target=51
    for name, fn, arr in [("Linear search",linear_search,data),("Binary search",binary_search,sorted_data)]:
        start=time.perf_counter(); idx=fn(arr,target); elapsed=(time.perf_counter()-start)*1_000_000
        print(f"{name}: index={idx} | {elapsed:.2f} microseconds")
