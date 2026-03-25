'''Check number in range'''

start,end = map(int, input("Enter the start and end point of range seprated by space : ").split())
num = int(input("enter the number for check in this range or not : "))

if start < end :
    if num in range(start,end):
        print(f"Number {num} lies in range {start} to {end}")
    else:
        print(f"Number {num} not lies in range {start} to {end}")

elif start > end :
    if num in range(end,start):
        print(f"Number {num} lies in range {end} to {start}")
    else:
        print(f"Number {num} not lies in range {end} to {start}")

else:
    print("Enter a valid range")