''' The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.'''


import json
from json.decoder import JSONDecodeError


def get_stored_username():

    filename = 'user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return None
    else:
        return username
    
def get_username():
    filename = 'user.json'
    username = input("Enter your name : ")
    with open(filename,'w') as f:
        json.dump(username,f)
    return username



def greet_user():
    filename = 'user.json'
    username = get_stored_username()
    if username:
        user = input(f"{username} is this correct username for not 'n' : ")
        if user.lower() == 'n':
            username = get_username()
            print("We'll remember when you come back ",username)

        else:    
            print("Welcome back, ",username)
    else:
        username = get_username()
        print("We'll remember when you come back ",username)
        
        
greet_user()
