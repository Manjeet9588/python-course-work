'''Write a program that prompts for the user’s favorite number. Use json.dump() 
to store this number in a file. Write a separate program that reads in this 
value and prints the message, “I know your favorite number! It’s _____.”'''

import json 

filename = 'fav_num.json'
fav_num = int(input("Enter your fav number : "))
with open(filename,'w') as f:
    json.dump(fav_num,f)

with open(filename) as f:
    num = json.load(f)
    print("I know your favorite number! It’s ",num)
