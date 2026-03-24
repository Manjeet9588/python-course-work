''''Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different 
location on your system, and make sure the code in the except block executes properly.'''

cats = 'cats.txt'
dogs = '/home/khatri/Desktop/pla/Python cash course/chapter 10/practice/dogs.txt'

try:
    with open(cats) as cat_file:
        cat_names = cat_file.readlines()

except FileNotFoundError:
    print(f"The file {cats} is not found")

else:
    print("For cat names : ")
    for cat_name in cat_names:
        print(cat_name.strip())


try:    
    with open(dogs) as dog_file:
        dog_names = dog_file.readlines()

except FileNotFoundError:
    print(f"The file {dogs} is not found")

else:
    print("\nfor dog names : ")
    for dog_name in dog_names:
        print(dog_name.strip())