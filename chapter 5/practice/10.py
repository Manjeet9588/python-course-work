'''Rock-paper-scissors logic'''

import random

sign = ['r','p','s']
while True:
    bot = random.choice(sign)
    user = input("Enter your sign rock 'r' , paper 'p', scissors 's' and quit 'q' : ")
    user = user.lower()
    if user == 'q':
        break
    if user == bot :
        print(f"Draw both chose same")
    elif user == 'r' and bot == 'p':
        print("you loss \nyou chose rock and bot chose paper")
    elif user == 'r' and bot == 's':
        print("you won \nyou chose rock and bot chose scissors")
    elif user == 'p' and bot == 'r':
        print("you won \nyou chose paper and bot chose rock")
    elif user == 'p' and bot == 's':
        print("you loss \nyou chose paper and bot chose scissors")
    elif user == 's' and bot == 'r':
        print("you loss \nyou chose scissors and bot chose rock")
    elif user == 's' and bot == 'p':
        print("you won \nyou chose scissors and bot chose paper")
    else:
        print("Enter a valid input")