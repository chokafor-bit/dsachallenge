def move_zeros(numbers):
    result = []       #  Initialize a result list and a zero counter

    zero_count = 0
    
    for num in numbers:      # Loop through the list and separate zeros from non-zeros

        if num != 0:
            result.append(num)
        else:
            zero_count += 1
            
    result.extend([0] * zero_count)      #  Append the collected zeros to the end of the result list

    
    return result      #  Return the final list



print(move_zeros([0, 1, 0, 3, 12]))

print(move_zeros([1, 2, 3]))

print(move_zeros([0, 0, 5]))