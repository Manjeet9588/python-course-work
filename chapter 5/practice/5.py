'''Ticket pricing system (age-based)'''

while True:
    age = input("Enter your age or 'q' for quit : ")
    if age == 'q':
        break
    elif int(age) < 12:
        print("The Ticket is free")
    elif 12<= int(age) < 20:
        print("The Ticket is 5$")
    elif 20<= int(age) < 30:
        print("The Ticket is 10$")
    else:
        print("The Ticket is 15$")
                