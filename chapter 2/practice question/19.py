'''Swap two numbers without using third variable'''
a = 10
b = 5
print(f"Before swap value of a is {a} and b is {b}")
a = a+b
b = a-b
a = a-b
print(f"After swap value of a is {a} and b is {b}")