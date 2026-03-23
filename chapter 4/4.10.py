'''Using one of the programs you wrote in this chapter, add several lines to 
the end of the program that do the following:
•Print the message, The first three items in the list are:. Then use a slice 
to print the first three items from that program’s list.
•Print the message, Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
•Print the message, The last three items in the list are:. Use a slice to print 
the last three items in the list.'''

fav_fruits = ['apple','banana','mango','pinapple','grapes']
print(fav_fruits)

print(f"The First three item in the list are {fav_fruits[:3]}")

print(f"The middle three iyem in the list are {fav_fruits[1:4]}")

print(f"The last three item in the list are {fav_fruits[-3:]}")