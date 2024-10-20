# dyPi/__init__.py


def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    if n <= 0:
        raise ValueError("Fibonacci sequence length must be a positive integer.")
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
