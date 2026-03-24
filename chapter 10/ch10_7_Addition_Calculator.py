'''Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.'''

while True:
    try:
        first = input("Enter your first number or 'q' for quit : ")
        if first.lower() == 'q':
            break
        second = input("Enter your second number or 'q' for quit : ")
        if second.lower() == 'q':
            break
        result = int(first) + int(second)
    except ValueError:
        print("Enter a valid number")
    else:
        print(result)