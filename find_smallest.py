

def find_smallest(numbers):
    #handle the edge cases for empty list 
    if not numbers:
        return None 

    # Initailize our tracker with the first element 
    smallest  =  numbers[0]

    # the loop  the remaining numbers and cmpare 
    for num in numbers[1:]:
        if num < smallest: 
            smallest = num 

    # return the final result 
    return smallest          
print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))