'''Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding 
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.'''

def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i].title()


magicians_name = ['ashok','ramesh','madan']
make_great(magicians_name)
show_magicians(magicians_name)
