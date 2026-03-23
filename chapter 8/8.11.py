'''Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original 
names and one list with the Great added to each magician’s name'''

def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i].title()
    return magicians

magicians_name = ['ashok','ramesh','madan']
new_list = make_great(magicians_name[:])
show_magicians(new_list)

show_magicians(magicians_name)
