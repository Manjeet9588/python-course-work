'''You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.'''

invite_list = ['Asmit','Ashu','Rahul']
print("I found a big table for our party so some other guset also invited")
invite_list.insert(0,'Amit')
invite_list.insert(3,'Jahanvi')
invite_list.append('Prince')
print(f"Hey {invite_list[0].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[1].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[2].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[3].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[4].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(f"Hey {invite_list[5].capitalize()} hey today is my birthday and you are invited in my birthday party")
print(invite_list)
