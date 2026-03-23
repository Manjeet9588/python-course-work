'''Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich 
that is being ordered. Call the function three times, using a different number of arguments each time.'''
def sandwich(*items):
    print("The summary of your ordered sanwich is : ")
    for i in items:
        print(i)

order_number = int(input(("How many person are there : ")))
for _ in range(order_number):
    order = [item.strip() for item in input("Enter your sandwich item seprated by ',' : ").split(",")]
    sandwich(*order)


