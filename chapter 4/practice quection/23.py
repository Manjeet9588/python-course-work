'''Right Aligned Triangle'''

num = int(input("Enter your right aligned triangle length : "))

for n1 in range(1,num+1):
    for n2 in range(num,n1-1,-1):
        print(end=" ")
    print("*"*n1)