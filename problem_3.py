def list_sum(numbers):
    # initailize an accumulator variable (handles empty list by returning 0)
    total = 0

    # loop through the list and add each to the total 
    for num in numbers:
        total += num 

    # return the final total 
    return total     

print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))






