def move_zeros(numbers):
    # pass 
    insert_pos = 0
    for num in numbers:
        if num  != 0:
            numbers[insert_pos] = num
            insert_pos += 1

    for i in range(insert_pos, len(numbers)):
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