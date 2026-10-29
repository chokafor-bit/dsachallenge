def find_number(numbers, target):
    for index, num in enumerate(numbers):          #  Loop through the list with indices and check for a match
   
        if num == target:
            return index                   #  Return the index immediately on the first occurrence

    return  -1                     # Return -1 if the target was not found in the list 



print(find_number([10, 25, 30, 45], 30))

print(find_number([5, 8, 5, 9], 5))

print(find_number([10, 20, 30], 99))