'''Find the second largest number in a list.'''
number = [1,2,3,4,5,6,7,8,9]

#solution 1
print(f"The second largest number in a list is {sorted(number)[-2]}")

# solution 2
largest = number[0]
second_largest = number[0]

for num in number:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("The second largest number is", second_largest)






