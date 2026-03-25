import json

def greet_user(filename):
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Enter your name : ")
        with open(filename,'w') as f:
            json.dump(username,f)
            print("we'll remember you!")
    else:
        print("Welcome back, ",username)

greet_user('user.json')