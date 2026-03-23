'''Write a program that asks the user how many people are in their dinner group. 
If the answer is more than  eight, print a message saying they’ll have to wait for a table. 
Otherwise, report that their table is ready.'''

people_number = int(input("How many people are in their dinner group : "))
if people_number > 8:
    print("You'll have to wait for a table.")
elif people_number == 8:
    print("Your table is ready immediately.")
else:
    print("Your table is ready.")