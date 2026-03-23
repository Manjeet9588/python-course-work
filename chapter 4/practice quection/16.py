'''Count Prime Numbers in Range'''

start = int(input("Enter the number where the range start : "))
end = int(input("Enter the number where the range end : "))

count = 0
if(start < 0 or end < 0):
    print("Enter a positive range")
elif(start < end):
    for num in range(start,end):
        if(num <=1):
            prime = False
        elif(num > 1):
            prime = True
            for n in range(2,int(num**0.5)+1):
                if(num % n == 0):
                    prime = False
                    break
        if prime:
            count += 1

    print(f"The prime number is the range {start} and {end} is {count}")

else:
    print("Enter a valid range")



