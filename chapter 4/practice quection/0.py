'''Inverted Right Triangle'''

num = int(input("Enter your inverted right triangle : "))

for n1 in range(num,0,-1):
    for n2 in range(n1,0,-1):
        print("*", end=" ")
    print()



'''Number Triangle'''

num = int(input("Enter your length of number triangle : "))

for n1 in range(1,num+1):
    for n2 in range(1,n1+1):
        print(f"{n2}",end=" ")
    print()


''''Same Number Triangle'''

num = int(input("Enter length of same number triangle : "))

for n1 in range(1,num+1):
    for n2 in range(n1,n1+1):
        print(f"{n2}"*n2,end=" ")
    print()



'''Reverse Number Triangle'''

num = int(input("Enter length of reverse number triangle : "))

for n1 in range(num,0,-1):
    for n2 in range(1,n1+1):
        print(f"{n2}",end=" ")
    print()



'''Continuous Numbers triangle'''

num = int(input("Enter the length of continous numbers triangle : "))
n = 1
m = 1
for n1 in range(1,num+1):
    n = n + n1
    for n2 in range(m,n):
        print(f"{n2}",end=" ")
    m = m + n1
    print()



'''Right Aligned Triangle'''

num = int(input("Enter your right aligned triangle length : "))

for n1 in range(1,num+1):
    for n2 in range(num,n1-1,-1):
        print(end=" ")
    print("*"*n2)