'''Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program'''

fav_num = {}
number = int(input("Enter number of people : "))
for _ in range(number):
    name = input("Enter name : ").strip().title()
    num = int(input("Enter fav number : "))
    fav_num[name] = num

for index, (name , num) in enumerate(sorted(fav_num.items()),  start = 1):
    print(f"{index}. {name} - {num}")