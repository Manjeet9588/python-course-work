'''Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.'''

info_1 = {'Name':'Manjeet','age':20,'city': 'Narnaul'}
info_2 = {'Name':'Amit','age':23,'city': 'Narnaul'}
info_3 = {'Name':'Shubham','age':18,'city': 'Narnaul'}

people = [info_1,info_2,info_3]
count = 1
for info in people:
    print(f"\nInformation of person {count}")
    for key , value in sorted(info.items()):
        print(f"\t{key} is {value}")
    count += 1