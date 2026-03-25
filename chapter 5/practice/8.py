'''Check valid password'''

password = input("Enter your password i tell it valid or invalid : ")


upper = False
lower = False
digit = False
special = False
for char in password:
    if char.isupper():
        upper = True
    elif char.islower():
        lower = True
    elif char.isdigit():
        digit = True
    elif not char.isalnum():
        special = True

if upper and lower and digit and special:
    print("The password is valid")

else: 
    print("The password is invalid")
    print("the password must contain upper char, lower char, digit and a special char")
    
