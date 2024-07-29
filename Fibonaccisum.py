def fibonacci_sum(K):
    fib_sum = 0
    fib_prev = 0
    fib_curr = 1

    for _ in range(K):
        fib_sum += fib_curr
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    return fib_sum

# Read input value K
K = int(input())

# Calculate the sum of the first K Fibonacci numbers
sum_result = fibonacci_sum(K)

# Output the result
print(sum_result)
