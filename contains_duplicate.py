def has_duplicates(numbers):
    seen = set() #  Initialize a "Seen" tracker set for fast O(1) lookups

    for num in numbers: #  Loop through the list
        if num in seen: #  Check if already seen; return True if a duplicate is found

            return True 

        seen.add(num) # Add the number to our tracker set
    
    return False # Return False if the loop finishes with no duplicates

print(has_duplicates([1, 2, 3, 2]))

print(has_duplicates([1, 2, 3, 4]))

print(has_duplicates([]))