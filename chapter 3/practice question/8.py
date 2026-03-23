'''Reverse a list without using reverse() or slicing.'''
number = [1,2,3,4,5,6,7,8,9]
reverse = []
for num in number:
    reverse.insert(0,num)

number = reverse
print(number)
