def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Example usage:
n = 10
fib_sequence = fibonacci_iterative(n)
print(f"The first {n} Fibonacci numbers are:", fib_sequence)
