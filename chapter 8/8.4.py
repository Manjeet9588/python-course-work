''' Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.'''

def make_shirt(size="Large",message="I Love Python"):
    print(f"The size of shirt is {size.title()} and the message printed is {message}")

make_shirt(size="large")
make_shirt(size="medium")
make_shirt(size="small",message="that's the thing i want")