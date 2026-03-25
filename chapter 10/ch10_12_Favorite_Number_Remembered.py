'''Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.'''


import json
from json.decoder import JSONDecodeError

filename = 'fav_num.json'
try :
    with open(filename) as f :
        num = json.load(f)
        if isinstance(num, int) :
            print("I know your favorite number! It’s ",num)
        else:
            fav_num = int(input("Enter your fav number : "))
            with open(filename,'w') as f:
                json.dump(fav_num,f)
            
except (FileNotFoundError, JSONDecodeError):
    fav_num = int(input("Enter your fav number : "))
    with open(filename,'w') as f:
        json.dump(fav_num,f)