def reverse_list(items):
    result = [] # empty list 
    
    # len(items) finishes first, then we subtract 1, stop at -1, step by -1
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
        
    return result


print(reverse_list([1, 2, 3, 4]))
print(reverse_list(["a", "b", "c"]))