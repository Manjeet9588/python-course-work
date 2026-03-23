''''Same Number Triangle'''

num = int(input("Enter length of same number triangle : "))

for n1 in range(1,num+1):
    for n2 in range(n1,n1+1):
        print(str(n1)*n1)