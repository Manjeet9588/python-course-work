'''ATM withdrawal logic'''

balance = 10000
pin = 1234

while True:
    print("1. Balance")
    print("2. Credit")
    print("3. Withdrawal")
    user = input("'q' quit  : ")
    
    if user == '1':
        print(f"The Balance is : {balance}")
    
    elif user == '2':
        credit_amount = input("Enter credit amount allow only in integer form: ")
        if credit_amount.isdigit():
            balance = balance + int(credit_amount)
            print(f"The updated balance is {balance}")
        else :
            print("Enter a valid credit amount")
    
    elif user == '3':
        withdrawal = int(input("Enter withdral amount: "))
        if withdrawal <= balance:
            balance = balance - int(withdrawal)
            print("The withdrawal is succesfull")

        else:
            print("The withdrawal is unsuccesfull")

    elif user == 'q':
        break
