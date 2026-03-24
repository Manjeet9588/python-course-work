'''Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by 
reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.'''

#Method 1 : Read entire file
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
#Method 2 : Looping over the file_object    
with open('learning_python.txt') as file_object:
    for content in file_object:
        print(content.rstrip())

#Method 3 : storing lines in a list
with open('learning_python.txt') as file_object:
    contents = file_object.readlines()

for line in contents:
    print(line.rstrip())
    
    
