def digit_sum(number):
    """Return the sum of the digits of a non-negative integer."""
    return sum(int(digit) for digit in str(abs(number)))


def count_equal_digit_sum_pairs(nums):
    """
    Count pairs (i, j) where i < j and nums[i], nums[j]
    have the same digit sum.
    """
    frequencies = {}
    pairs = 0

    for number in nums:
        total = digit_sum(number)
        # Every earlier number with this digit sum makes one new pair.
        pairs += frequencies.get(total, 0)
        frequencies[total] = frequencies.get(total, 0) + 1

    return pairs


def solve():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    if len(nums) != n:
        raise ValueError(f"Expected {n} numbers, received {len(nums)}")
    print(count_equal_digit_sum_pairs(nums))


if __name__ == "__main__":
    # Sample from the provided Lab Sheet 10A:
    # 51 and 42 both have digit sum 6; 71 and 17 both have digit sum 8.
    # Therefore the explanation gives 2 pairs, even though the printed
    # sample output in the handout says 8.
    solve()
