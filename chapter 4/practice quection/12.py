'''Check if triangle is valid.'''
n1 = int(input("Enter first side of triangle : "))
n2 = int(input("Enter second side of triangle : "))
n3 = int(input("Enter third side of triangle : "))

if(n1+n2>n3 and n1+n3>n2 and n2+n3>n1):
    print("Your triangle is valid")
else:
    print("Your triangle is invalid")