def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    
    # Your code here
    length_list1 = len(L1)
    length_list2 = len(L2)
    
    if length_list1 == 0 and length_list2 == 0:
        return (None, None, None)
    
    if length_list1 != length_list2:
        return False
    
    list1_dict = {}
    list2_dict = {}
    
    for item in L1 :
        if item not in list1_dict:
            list1_dict[item] = 1
        else:
            list1_dict[item] +=1


    for item in L2 :
        if item not in list2_dict:
            list2_dict[item] = 1
        else:
            list2_dict[item] +=1
            
    if list1_dict != list2_dict:
        return False    
    
    max_key = max(list1_dict, key=list1_dict.get) 
    max_value = list1_dict[max_key] 
    return (max_key, max_value, type(max_key))  
    
    
L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']
print(is_list_permutation(L1,L2))
# L2 = ['a', 'b']
# L1 = ['a', 'a', 'b']
    