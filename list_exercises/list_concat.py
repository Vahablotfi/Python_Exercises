"""
Problem 1: Calculating the Dot Product of Two Lists
Explanation:
The dot product of two lists of numbers is the sum of the pairwise products of their corresponding elements. If you have two lists of equal length, such as listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is calculated as:

1*4 + 2*5 + 3*6 = 32

You will traverse both lists in parallel, multiply corresponding elements, and accumulate the results to get the final sum. This method is commonly used in linear algebra and machine learning.

Instructions:
1. Define the function dotProduct(listA, listB), which takes two lists of the same length as inputs.
2. Initialize a variable sum to 0, which will store the running total of the pairwise products.
3. Iterate through both lists using their indices (since both lists have the same length):
  - Multiply the corresponding elements from listA and listB.
  - Add the result to sum.
4. Return sum as the final result.
"""