'''Find greatest of two numbers'''

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))

if(num1<num2):
    print(f"The second number {num2} is greater")
elif(num1>num2):
    print(f"The first number {num1} is greater")
else:
    print("both number are equal")