'''Modify your except block in Exercise 10-8 to fail
silently if either file is missing.'''


cats = 'cat.txt'
dogs = '/home/khatri/Desktop/pla/Python cash course/chapter 10/practice/dogs.txt'

try:
    with open(cats) as cat_file:
        cat_names = cat_file.readlines()

except FileNotFoundError:
    pass
else:
    print("For cat names : ")
    for cat_name in cat_names:
        print(cat_name.strip())


try:    
    with open(dogs) as dog_file:
        dog_names = dog_file.readlines()

except FileNotFoundError:
    pass
else:
    print("\nfor dog names : ")
    for dog_name in dog_names:
        print(dog_name.strip())