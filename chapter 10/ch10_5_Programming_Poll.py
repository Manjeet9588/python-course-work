'''Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.'''

filename = 'reason.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input("Enter your name or 'q' for quit :").strip()
        if name.lower() == 'q':
            break
        if not name:
            continue

        reason = input("Enter reason why you love programming or 'q' for quit : ").strip()
        
        if reason.lower() == 'q':
            break
        if not reason:
            reason = 'Not Mention'
        file_object.write(f"Name : {name.title()}\n\tReason : {reason}\n\n")
