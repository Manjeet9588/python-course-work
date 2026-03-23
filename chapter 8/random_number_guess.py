'''Mini Number Guessing Game
Random number
User guesses
Give hints (higher/lower)'''

import random

number = random.randint(1,11)
while True:
    user = int(input("Guess (1–10): "))
    
    if user == number:
        print("Correct!")
        break
    elif user < number:
        print("Higher")
    else:
        print("Lower")