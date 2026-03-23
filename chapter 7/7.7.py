''' Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)'''

num = int(input("Enter a number : "))

while True:
    print(f"{num}",end=' ')
    num += 1

