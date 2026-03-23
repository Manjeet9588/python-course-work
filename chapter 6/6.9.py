'''Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.'''

favorite_places = {'Manjeet':['Manali','thailand','goa']}

n = int(input("How many people are there : "))

for _ in range(n):
    name = input("Enter your name : ")
    places = list(set(input("Enter your favorite place seprated by space: ").split()))
    unique_place = []
    for place in places:
        if place not in unique_place:
            unique_place.append(place)
    favorite_places[name] = unique_place
for key , value in sorted(favorite_places.items()):
    print(f"\n{key.title()} favorite place are :")
    for place in value :
        print("\t"+place.title())
        