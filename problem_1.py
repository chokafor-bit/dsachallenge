

def find_largest(numbers):
    #handle the edge cases for empty list 
    if not numbers:
        return None 

    # Initailize our tracker with the first element 
    largest =  numbers[0]

    # the loop  the remaining numbers and cmpare 
    for num in numbers[1:]:
        if num > largest: 
            largest = num 

    # return the final result 
    return largest


print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))