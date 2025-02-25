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

def dotProduct(listA, listB):
  """    
        Calculates the dot product of two lists.

    Args:
        listA (list): A list of numbers.
        listB (list): A list of numbers of the same length as listA.

    Returns:
        int or float: The sum of the pairwise products of listA and listB.

    Examples:
        >>> dotProduct([1, 2, 3], [4, 5, 6])
        32

        >>> dotProduct([0, 0, 0], [1, 2, 3])
        0

        >>> dotProduct([1, -2, 3], [-4, 5, -6])
        -32

        >>> dotProduct([1.5, 2.5], [3.0, 4.0])
        13.0

        >>> dotProduct([], [])
        0

        >>> dotProduct([1], [2])
        2
  """
  sum = 0
  
  for i in range(len(listA)):
    sum+= listA[i] * listB[i]
    
  return sum

listA=[1,2,3]
listB=[4,5,6]
print(dotProduct(listA, listB))
  
  