''' A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
•Use a for loop to print each food the restaurant offers.
•Try to modify one of the items, and make sure that Python rejects the change.
•The restaurant changes its menu, replacing two of the items with different 
foods. Add a block of code that rewrites the tuple, and then use a for loop 
to print each of the items on the revised menu.'''

food_list = ('maggie','burger','pizza','french frize','momoos')
print("The old menu is :")
for food in food_list:
    print(food)

print("\nThe new menu is :")
food_list = ('colddrik','burgure','ice cream','french frize','momose')
for food in food_list:
    print(food)