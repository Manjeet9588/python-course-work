'''Check leap year'''


year = int(input("Enter year to check is it leap year or not : "))
if year%4 == 0:
    if year%100 == 0 and year%400 != 0:
        print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")