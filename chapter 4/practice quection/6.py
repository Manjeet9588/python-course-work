'''Check if year is leap year.'''
year = int(input("Enter your year : "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Entered year is a leap year")
        else:
            print("Entered year is not a leap year")
    else:
        print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")