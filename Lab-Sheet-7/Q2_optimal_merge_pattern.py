import heapq

def optimal_merge(sizes):
    heap = list(sizes); heapq.heapify(heap); total = 0; steps = []
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        merged = a + b; total += merged; steps.append((a, b, merged)); heapq.heappush(heap, merged)
    return steps, total

if __name__ == "__main__":
    sizes = [5, 10, 20, 30]
    steps, cost = optimal_merge(sizes)
    for a, b, merged in steps: print(f"{a} + {b} = {merged}")
    print("Minimum total cost:", cost)
