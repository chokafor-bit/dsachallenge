def find_number(numbers, target):
    #  Loop through the list with indices and check for a match
    for index, num in enumerate(numbers):
        if num == target:
            #  Return the index immediately on the first occurrence
            return index 
            # Return -1 if the target was not found in the list 
    return  -1       


print(find_number([10, 25, 30, 45], 30))

print(find_number([5, 8, 5, 9], 5))

print(find_number([10, 20, 30], 99))