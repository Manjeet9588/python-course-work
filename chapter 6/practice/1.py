'''Count frequency of characters in string'''

line = input("Enter your string : ")
char = input("Enter char which frequency you want to find : ")
count = 0
len_char = len((char))
length = len(line)
for c in range(0,length,len_char):
    if line[c:c+len_char] == char:
        count += 1

print(f"The frequency of {char} in your string is {count}")
