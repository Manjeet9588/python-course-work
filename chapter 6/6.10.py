'''Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.'''

fav_num ={}
n = int(input("How many people are there : "))
for _ in range(n):
    name = input("Enter your name : ")
    numbers = list(set(input("Enter your favourate numbers seprated by space : ").split()))
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    fav_num[name] = unique_numbers

for key,values in fav_num.items():
    print(key + ":")
    for value in values:
        print("\t" + value )


