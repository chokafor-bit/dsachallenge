

def find_smallest(numbers):
    if not numbers:               #handle the edge cases for empty list 

        return None 

    smallest  =  numbers[0]            # Initailize our tracker with the first element 
 

    for num in numbers[1:]:                     # the loop  the remaining numbers and cmpare 

        if num < smallest:        # if the smallest number is less 
            smallest = num 

    return smallest                                      # return the final result 





print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))