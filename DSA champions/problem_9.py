def first_duplicate(numbers):
    seen = set()    # Initialize a "Seen" tracker set

    
    for num in numbers:    # Loop through the list left-to-right and check the tracker

        if num in seen:
            return num     #  Return immediately if we hit a duplicate

        
        seen.add(num)    #  Add to the tracker if not seen yet

        
    return None      # Return None if no duplicates are found


print(first_duplicate([4, 7, 2, 7, 5, 4]))

print(first_duplicate([1, 2, 3, 4]))  

print(first_duplicate([5, 5, 3]))