def length_of_lis(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # dp[i] will be the length of the LIS ending at index i

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
sequence = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(sequence))  # Output: 4
