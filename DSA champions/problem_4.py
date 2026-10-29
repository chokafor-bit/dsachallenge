def count_even(numbers):
    count = 0                # initailize an accumulator variable to set the count to 0 

    for num in numbers:
        if num % 2 == 0:   # we need the mudolus to get the even numbers

            count += 1   # we move to the next number if not found 
            
    return count     # we returned the final result after the process 

print(count_even([1, 2, 3, 4, 6]))
print(count_even([1, 3, 5, 7]))