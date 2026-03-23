'''Rotate a list to the right by 1 position.
Example: [1,2,3,4] → [4,1,2,3]'''

number = [1,2,3,4,5,6]
print(f"The old list is {number}")
num = number.pop(-1)
number.insert(0,num)
print(f"The new list is {number}")