'''Check if number is palindrome.'''

num = int(input("Enter your number : "))
rev = 0
tem = num
while(tem > 0):
    digit = (tem % 10)
    rev = (rev * 10 ) + digit
    tem //= 10
if(rev == num):
    print(f"The entered number {num} is a palindrome")
else:
    print(f"The entered number {num} is not a palindrome")