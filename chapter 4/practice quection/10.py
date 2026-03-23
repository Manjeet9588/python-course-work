'''Write a program to check if a number is prime.'''

num = int(input("Enter your number : "))

if(num <= 1):
    print("The entered number is not a prime number")

else:
    prime = True
    for n in range(2,num//2):
        if(num % n == 0):
            prime = False
            break

    if prime:
        print("The entered number is a prime number")
    else:
        print("The entered number is not a prime number")

