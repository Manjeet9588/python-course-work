'''Number guessing logic.'''
import random
guss = random.randint(0,9)
user = int(input("Gussing a number between 0 to 9 : "))

if(user == guss):
    print("You gussing the right")
else:
    print("Your gussing is wrong ")