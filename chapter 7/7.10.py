''' Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.'''


poll = {}

while True:
    name = input("Enter your name or quit : ")
    name = name.title()
    if name.lower() == 'quit':
        break
    place = input("If you could visit one place in the world, where would you go? ")
    if name in poll:
        poll[name].append(place)
    else:
        poll[name] = [place]

print("\nPoll Results :")
for name , place in poll.items():
    print(f"{name} wants to visit {place}")