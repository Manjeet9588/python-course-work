'''Write program:
Check if number is prime'''

number = int(input("Enter your number : "))
prime = True
if number > 0:
    if number == 1:
        prime = False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            prime = False
            break

    if prime:
        print("the number is prime")
    else:
        print("The number is not a prime number") 

else:
    print("Enter postive or correct number")