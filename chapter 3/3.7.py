'''You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program'''

print("There are some issue so i can invite only 2 peroson ")

invite_list = ['Amit', 'Asmit', 'Ashu', 'Jahanvi', 'Rahul', 'Prince']
not_invited = invite_list.pop(1)
print(f"sorry {not_invited} i can not invite you for some reason")
not_invited = invite_list.pop(1)
print(f"sorry {not_invited} i can not invite you for some reason")
not_invited = invite_list.pop(1)
print(f"sorry {not_invited} i can not invite you for some reason")
not_invited = invite_list.pop(1)
print(f"sorry {not_invited} i can not invite you for some reason")

print(f"{invite_list[0]} you are still invited in my birthday party")
print(f"{invite_list[1]} you are still invited in my birthday party")

del invite_list[1]
del invite_list[0]
print(invite_list)