'''You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. Add a print statement at the end of your program stating the name of the 
 guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in your list'''

invite_list = ['Asmit','Ashu','Amrit']

not_comming = invite_list.pop(2)
invite_list.append('Rahul')

print(f"unfortunally {not_comming} is not comming")
print(f"Hey {invite_list[0].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[1].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[2].capitalize()} hey today is my birthday and you are invited in my birthday party")
