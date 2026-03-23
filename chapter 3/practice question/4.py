'''Find the length of a list without using len() (hint: loop counter).'''

number = [1,2,3,4,5,6,4,8,9]

count = 0
for num in number:
    count = count +1

print(count)