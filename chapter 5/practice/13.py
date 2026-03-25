'''Check divisible by multiple numbers'''

num = int(input("Enter your number : "))
numbers = [int(n) for n in input(f"Enter your numbers for check multiple of {num} or not : ").split()]
numbers = sorted(numbers)
multiple = []
not_multiple = []
for number in numbers:
    if number % num == 0 :
        multiple.append(number)
    else:
        not_multiple.append(number)

print(f"The numbers which is multiple of {num} is {multiple}")
print(f"The numbers which is not multiple of {num} is {not_multiple}")