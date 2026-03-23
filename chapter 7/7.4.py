'''Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

pizza_toppings = []
topping_active = True
while topping_active:
    topping = input("Enter topping : ")
    pizza_toppings.append(topping)
    repated = input("you’ll add that topping to their pizza. or quit : ")
    if repated == 'quit':
        topping_active = False
print(pizza_toppings)