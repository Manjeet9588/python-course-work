'''Count how many even numbers are in a list.'''

number = [1,2,3,4,5,6,7,8,9]
count = 0
for num in number:
    if(num%2==0):
        count+=1
print(f"The number of even numbers in list is {count}")