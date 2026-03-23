'''Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''

def make_shirt(size="L",message="I Love Python"):
    print(f"The size of shirt is {size.title()} and the message printed is {message}")

size = input("Enter the size of shirt alphabaticly : ")
message = input("Enter the message which will print on shirt : ")
make_shirt(size,message)
make_shirt(message=message,size=size)