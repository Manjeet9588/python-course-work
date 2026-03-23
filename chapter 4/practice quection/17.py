'''print a right angle triangel'''

num = int(input("Enter your length of triangle : "))

for n1 in range(1, num+1):
    for n2 in range(1,n1+1):
        print("*",end="")
    print()