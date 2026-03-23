'''Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.'''

def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())

magicians_name = ['ashok','ramesh','madan']
show_magicians(magicians_name)
