def move_zeros(numbers):
    # pass 
    insert_pos = 0   # created a variable insert_pos and set it to 0 
    for num in numbers:  # loop through the numbers in the given list
        if num  != 0:    # if num is not equal to 0
            numbers[insert_pos] = num   # we insert the position 
            insert_pos += 1       # and increment it by 1

    for i in range(insert_pos, len(numbers)): #, we used a loop to calculate the pos and len of numbers and index it to the first number 
        numbers[i] = 0 



list1 = [0, 1, 0, 3, 12]
move_zeros(list1)
print(list1)  

list2 = [4, 0, 5, 0, 2]
move_zeros(list2)
print(list2)  

list3 = [1, 2, 3]
move_zeros(list3)
print(list3)  