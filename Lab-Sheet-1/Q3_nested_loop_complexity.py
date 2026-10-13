import time

def quadratic_work(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

for n in (100, 500, 1000, 2000):
    start = time.perf_counter()
    operations = quadratic_work(n)
    elapsed = (time.perf_counter() - start) * 1000
    print(f"n={n:,} | operations={operations:,} | time={elapsed:.2f} ms")
print("The operation count grows as n squared, so time complexity is O(n^2).")
