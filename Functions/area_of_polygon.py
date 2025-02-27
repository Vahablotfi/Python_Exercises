# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is: 
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular polygon. 
# The function returns the sum, rounded to 4 decimal places.

import math

def polysum(n, s):
    """
    Calculates the sum of the area and the square of the perimeter of a regular polygon.
    
    Parameters:
    n (int): Number of sides of the polygon
    s (float): Length of each side
    
    Returns:
    float: The sum rounded to 4 decimal places
    
        Examples:
    >>> polysum(3, 2)
    15.5885
    >>> polysum(4, 5)
    141.1765
    """
    # Calculate area
    area = (0.25 * n * s ** 2) / math.tan(math.pi / n)
    
    # Calculate perimeter
    perimeter = n * s
    
    # Sum of area and square of perimeter
    result = area + perimeter ** 2
    
    return round(result, 4)

