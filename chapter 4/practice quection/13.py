'''ATM simulation (balance + withdraw).'''

balance = 10000
while True:
    num = int(input("1. check balance \n2. Withdraw money\n3. Deposit money \n4. Exit\n : "))
    if num == 1 :
        print(f"Your Balance is {balance}")

    elif num == 2 :
        withdraw = int(input("Enter your withdrawl amount : "))

        if(withdraw <= balance):
           print("Withdrawal amount is valid")
           print(f"After withdrawal the balance is {balance-withdraw}")
           balance = balance - withdraw
        else:
           print("Insufficient balance")

    elif num == 3:
        deposit = int(input("Enter your Deposit Value : "))
        balance = balance + deposit
    else:
        print("Thank you for using ATM")
        break

