from itertools import combinations

def find_subset_indices(nums, target):
    for r in range(1, len(nums) + 1):
        print(r)
        for indices in combinations(range(len(nums)), r):
            print(indices)
            if sum(nums[i] for i in indices) == target:
                return list(indices)
    return None

# Example usage
numbers = [3, 34, 4, 12, 5, 2]
target_value = 9
result = find_subset_indices(numbers, target_value)

if result:
    print(f"Indices of subset that adds up to {target_value}: {result}")
else:
    print(f"No subset adds up to {target_value}")
