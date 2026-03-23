'''Sort a list without using sort() (basic logic — try bubble sort idea).'''

number = [5,7,3,1,5,1,2,6,213,654,32,65,654]

for num in range(1,len(number)):
    for n1 in range(0,len(number)-num-1):
        if(number[n1]>number[n1+1]):
            number[n1],number[n1+1] = number[n1+1], number[n1]
print(number)