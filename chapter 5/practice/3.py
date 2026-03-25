'''Login system (basic)'''

username = "Manjeet"
password = 'khatri@123'

while True:
    print("'q' for quit anytime")
    user = input("Enter username : ").strip()
    if user == 'q':
        break
    
    if user == username:
        user_password = input("Enter password : ").strip()
        if user_password == 'q':
            break
        
        if user_password == password:
            print("Your login succesful")
        else :
            print("Incorrect password")
    
    else:
        print("Incorrect username try again")

