import json

filename = 'students_list.json'

with open(filename) as file:
    students = json.load(file)

loop_active = True
while loop_active:
    user = input("")
    while user.isdigit():
        loop_active = False
    if user :
        print(user)
    