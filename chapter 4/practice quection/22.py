'''Continuous Numbers triangle'''

num = int(input("Enter the length of continous numbers triangle : "))
end = 1
start = 1
for n1 in range(1,num+1):
    end = end + n1
    for n2 in range(start,end):
        print(f"{n2}",end=" ")
    start = start + n1
    print()