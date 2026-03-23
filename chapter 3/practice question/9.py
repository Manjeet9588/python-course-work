'''Remove duplicates from a list.'''

number = [2,5,1,8,1,5,2,1,5,1,6,5,1,6,5,1,1,6,5,1]
empty_list = []
for num in number:
    if num not in empty_list:
        empty_list.append(num)
print(empty_list)
