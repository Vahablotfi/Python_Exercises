"""
Calculate the Sum of the First N Natural Numbers (Using a Loop)
Explanation:
We want to calculate the sum of the first n natural numbers (1 + 2 + 3 + ... + n). This can be done by iterating from 1 to n and keeping track of the cumulative sum.

Concepts Covered:

For loops
Accumulator variables (total)
Instructions:
Write a function sum_n_iterative(n) that takes a positive integer n as input and returns the sum of the first n natural numbers.
Inside the function:
Initialize a variable total to 0.
Use a for loop to iterate from 1 to n.
In each iteration, add the current number to total.
Return the final value of total.
Test the function with several values of n (e.g., 5, 10, 100).
"""

def sum_n_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i             
    return total               


# Testing the function
print(sum_n_iterative(5))    # 1 + 2 + 3 + 4 + 5 = 15
print(sum_n_iterative(10))   # 55
print(sum_n_iterative(100))  # 5050