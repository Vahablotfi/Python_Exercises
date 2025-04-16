def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    value_dict = {}
    
    for value in aDict.values():
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
        
    single_keys=[]
        
    for key, value in aDict.items():
        if value_dict[value] == 1:  
            single_keys.append(key)
    
    return sorted(single_keys)
    