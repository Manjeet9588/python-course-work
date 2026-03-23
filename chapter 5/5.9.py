'''Add an if test to hello_admin.py to make sure the list of users is
not empty.
•If the list is empty, print the message We need to find some users!
•Remove all of the usernames from your list, and make sure the correct
message is printed.'''

user = ['admin','name','manjeet','vs']

if user:
    for username in user:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report")
        else:
            print(f"Hello {username}, thank you for logging in again")
user.clear()
if user :
    print("This is not an empty list")
else:
    print("We need to find some users!")