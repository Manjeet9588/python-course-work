'''Find the maximum number in a list (without max()).'''
number = [1,2,3,4,5,6,7,8,9]
max_num = number[0]
# solution 1
for num in number:
    if(max_num<=num):
        max_num = num
print(max_num)

#solution 2
num = sorted(number)
print(num[-1])