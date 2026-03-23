''' A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.'''

money_collection = 0
count = 0
while True:
    age = input("Enter your age or quit : ")
    if age.upper() == 'QUIT':
        break
    if age.isdigit():
        age = int(age)
        if age < 3 : 
            print("The ticket is free")
        elif 3 <= age <= 12:
            print("The ticket is $10")
            money_collection += 10
        else:
            print("The ticket is $15")
            money_collection += 15
        count += 1
    else:
        print("Enter a valid age or type quit")
    
print(f"The total money collected from {count} people is ${money_collection}")