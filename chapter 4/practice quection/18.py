'''Inverted Right Triangle'''

num = int(input("Enter your inverted right triangle : "))

for n1 in range(num,0,-1):
    for n2 in range(n1,0,-1):
        print("*", end=" ")
    print()