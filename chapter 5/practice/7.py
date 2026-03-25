'''Find largest of 4 numbers'''

numbers = [int(num) for num in input("Enter your numbers seprated by space : ").split()]
print(f"The largest number is {max(numbers)}")