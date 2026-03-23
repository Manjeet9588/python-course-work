'''Check if a person is eligible to vote (age >= 18).'''
age = int(input("Enter your age : "))

if(age <= 0):
    print("Enter valid age")
elif(age >= 18):
    print("Your are eligible to vote ")
else:
    print("Your are not eligible to vote")