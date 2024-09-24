def factorial_iterative(n):
    if n < 0:
        return "Invalid input! Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
n = 5
print(f"The factorial of {n} (iterative) is: {factorial_iterative(n)}")
