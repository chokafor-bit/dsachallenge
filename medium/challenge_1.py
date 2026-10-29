def second_largest(numbers):
    # pass
    largest = None
    second = None
    for num in numbers:  # we use loop to search through numbers
        if largest is None or num > largest:   # If we find a new  largest number
            second = largest
            largest = num 
        elif num < largest and (second is None or num > second):  # If num is strictly less than largest, check if it's bigger than our current second
            second = num 


    return second 


print(second_largest([10, 5, 8, 10, 3]))

print(second_largest([4, 4, 4]))

print(second_largest([-5, -2, -8, -3]))