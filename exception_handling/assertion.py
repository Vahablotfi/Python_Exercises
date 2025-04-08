"""
Defensive Programming with Assertions

The function calculates the average of a list of numbers.
However, it **does not check** for an empty list, causing a ZeroDivisionError.

Your task:
1. Use **assertions** to prevent dividing by zero.
2. Modify the function to **handle an empty list safely**.
3. Ensure that invalid inputs (non-numeric values) are also **properly handled**.
"""

import builtins
def calculate_average(grades):
    """Returns the average of a list of grades."""
    
        # Assert it's a list
    assert isinstance(grades, list)
    
    # Assert it's not empty
    assert len(grades) > 0

    # Assert all elements are numeric (int or float)
    assert all(isinstance(value, (int, float)) for value in grades)
    
    return builtins.sum(grades) / len(grades)


# Test Cases
print(calculate_average([80, 90, 100]))  # Expected: 90.0
print(calculate_average([80, "b", 100]))
print(calculate_average([]))  # Expected: ERROR!
 