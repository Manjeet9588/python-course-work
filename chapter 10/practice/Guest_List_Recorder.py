'''Write a Python program that repeatedly prompts the user to enter their name.
If the user enters 'q', the program should stop taking input.
If the user enters an empty name (just presses Enter or only spaces), the program should ignore it and ask again.
Each valid name should be written to a file called guest.txt.
The program should:
Preserve previous entries in the file
Store each name with a serial number (starting from 1 and continuing from existing entries)
After all inputs are completed, the program should display the contents of the file.'''


filename = 'guest.txt'
try:
    with open(filename) as file_object:
        Users = file_object.readlines()
    count = len(Users) + 1 
except FileNotFoundError:
    count = 1


with open(filename, 'a') as file_object:
    while True:
        name = input("Enter your name or 'q' for quit : ").strip()
        if name.lower() == 'q':
            break
        if not name:
            continue
        file_object.write(f"{count}. Name : {name.title()}\n")
        count += 1

with open(filename) as file_object:
    contents = file_object.readlines()

for user_name in contents:
    print(user_name.rstrip())