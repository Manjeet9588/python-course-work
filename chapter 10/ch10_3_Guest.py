'''Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.'''

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input("Enter your name or 'q' for quit : ").split()
        if name.lower() == 'q':
            break
        file_object.write(f"Name : {name.title()}\n")


with open(filename) as file_object:
    contents = file_object.readlines()

for user_name in contents:
    print(user_name.rstrip())