from collections import Counter

def digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))
def solve(nums):
    counts=Counter(digit_sum(value) for value in nums)
    return sum(count*(count-1)//2 for count in counts.values())

if __name__ == "__main__":
    n=int(input().strip())
    nums=list(map(int,input().split()))
    if len(nums)!=n: raise ValueError(f"Expected {n} numbers, got {len(nums)}")
    print(solve(nums))
