'''Simple calculator using operator input.'''
num1 = int(input("Enter your first number : "))
oper = input("Enter your operation : ")
num2 = int(input("Enter your second number : "))

operation = ['+','-','/','*','**','%','//']
if oper in operation:
    if(oper == '+'):
        print(num1 + num2)
    elif(oper == '-'):
        print(num1 - num2)
    elif(oper == '*'):
        print(num1 * num2)
    elif(oper == '/'):
        print(num1 / num2)
    elif(oper == '**'):
        print(num1 ** num2)
    elif(oper == '%'):
        print(num1 % num2)
    else:
        print(num1 // num2)
else:
    print("Enter a valid operation")