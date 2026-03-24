'''Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.'''

filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        guest_name = input("Enter your name or 'q' for quit : ").strip()
        if guest_name.lower() == 'q':
            break
        if not guest_name:
            continue
        greet = 'Hello, ' + guest_name.title()
        print(greet)
        file_object.write(f"{greet}\n")
        


