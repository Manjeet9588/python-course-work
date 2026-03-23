'''Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.'''

dog = {'name':'dog','owner': 'manjeet','bread':'buldog','age': '5','colour':'black'}
cat = {'name':'cat','owner': 'amit','bread':'desi','age': '3','colour': 'white'}
horse = {'name':'hourse','owner': 'shubham','bread':'african','age': '8','colour': 'brown'}
pets = [dog,cat,horse]

for pet in pets:
    print(f"\ninformation about {pet['name'].title()} is :")
    for key , value in sorted(pet.items()):
        print(f"\t{key.title()} is {value.title()}")
