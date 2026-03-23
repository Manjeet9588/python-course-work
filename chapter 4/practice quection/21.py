'''Reverse Number Triangle'''

num = int(input("Enter length of reverse number triangle : "))

for n1 in range(num,0,-1):
    for n2 in range(1,n1+1):
        print(f"{n2}",end=" ")
    print()