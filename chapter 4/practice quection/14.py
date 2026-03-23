'''Rock-paper-scissors logic.'''

import random
sign = ('Rock','Paper','Scissor')

while True:
    bot = random.choice(sign)
    user = int(input("1. Rock \n2. Paper \n3. Scissor \n4. Exit \nEnter your choice:"))
    if( user == 1 ):
        if (bot == 'Rock'):
            print("your choice is Rock and bot choice Rock \nThe match is draw")
        elif (bot == 'Paper'):
            print("your choice is Rock and bot choice paper \nBot won the match")
        else:
            print("your choice is Rock and bot choice Scissor \nYou won the match")
    elif ( user == 2):
        if (bot == 'Rock'):
            print("your choice is Paper and bot choice Rock \nYou won the match")
        elif (bot == 'Paper'):
            print("your choice is Paper and bot choice paper \nThe match is draw")
        else:
            print("your choice is Paper and bot choice Scissor \nBot won the match")
    elif ( user == 3): 
        if (bot == 'Rock'):
            print("your choice is Scissor and bot choice Rock \nBot won the match")
        elif (bot == 'Paper'):
            print("your choice is Scissor and bot choice paper \nYou won the match")
        else:
            print("your choice is Scissor and bot choice Scissor \nThe match is draw")    
    else:
        print("Thanks for playing")
        break