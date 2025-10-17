def stdDevOfLengths(lis_of_length):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
    or NaN if L is empty.
    """
    
    if not lis_of_length:
        return float("NaN")

        
    mean = sum(lis_of_length)/float(len(lis_of_length))
    total = 0.0
    
    for num in lis_of_length:
        total+= (num - mean)**2
    
    std = (total/len(lis_of_length))**0.5
    
    return std/mean
    
    
numbers_list=[10, 4, 12, 15, 20, 5]

print(stdDevOfLengths(numbers_list)) 
    