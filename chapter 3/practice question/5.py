'''Check if a number exists in a list.'''

number = [1,2,3,4,5,6,7,8,9]
check_number = int(input("Enter your number for check : "))
if check_number in number:
    print("The number exist in the list ")
else:
    print("The number does not exist in the list")
