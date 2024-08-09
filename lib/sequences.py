#!/usr/bin/env python3

# def print_fibonacci(length):
#     pass
def print_fibonacci(length):
    fibonacci_sequence = []
    
    if length <= 0:
        print(fibonacci_sequence)
        return
    
    # Starting values for the Fibonacci sequence
    a, b = 0, 1
    
    for _ in range(length):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    print(fibonacci_sequence)