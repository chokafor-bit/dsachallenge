def list_sum(numbers):
    total = 0                      # initailize an accumulator variable (handles empty list by returning 0)
     

    for num in numbers:            # loop through the list and add each to the total 
   
        total += num 

    return total                   # return the final total 


print(list_sum([2, 4, 6, 8]))
print(list_sum([-5, 10, -2]))
print(list_sum([]))






