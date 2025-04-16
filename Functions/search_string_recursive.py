def isIn(char, aStr):
    """
    Recursive function to determine if char is in aStr using bisection search.
    :param char: a single character to search for
    :param aStr: a sorted string
    :return: True if char is in aStr, False otherwise
    """
    # Base case: if the string is empty, return False
    if len(aStr) == 0:
        return False
    
    # Base case: if the string has one character, check if it's the target character
    if len(aStr) == 1:
        return aStr == char
    
    # Find the middle index
    mid_index = len(aStr) // 2
    mid_char = aStr[mid_index]
    
    # If the middle character is the one we're looking for, return True
    if char == mid_char:
        return True
    
    # If char is smaller than the middle character, search the left half
    elif char < mid_char:
        return isIn(char, aStr[:mid_index])
    
    # If char is greater than the middle character, search the right half
    else:
        return isIn(char, aStr[mid_index + 1:])

# Example usage
print(isIn('e', 'abcdefg'))  # True
print(isIn('z', 'abcdefg'))  # False