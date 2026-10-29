

def find_largest(numbers):
    if not numbers:    #handle the edge cases for empty list 

        return None 

    largest =  numbers[0]    # Initailize our tracker with the first element 


    for num in numbers[1:]:        # the loop  the remaining numbers and cmpare 
 
        if num > largest:         # if the  number is largest 
            largest = num 

    return largest                 # return the final result 
     


print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))