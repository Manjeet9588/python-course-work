''' Start with your program from Exercise 4-1(page 60). Make a copy of the 
list of pizzas, and call it friend_pizzas. Then, do the following:
•Add a new pizza to the original list.
•Add a different pizza to the list friend_pizzas.
•Prove that you have two separate lists. Print the message, My favorite 
pizzas are:, and then use a for loop to print the first list.  Print the 
message, My friend’s favorite pizzas are:, and then use a for loop to print 
the second list. Make sure each new pizza is stored in the appropriate list.'''

pizza_list = ['onion chees pizza','double chees pizza','pepperoni pizza']
friend_pizza = pizza_list[:]

pizza_list.append('corn pizza')
friend_pizza.append('rosted flavor pizza')
print(f"pizza_list = {pizza_list} \nfriend_pizza = {friend_pizza}")

print("\nMy favorite pizzas are :")
for pizza in pizza_list:
    print(pizza)

print("\nmy friend's favorite pizzas are :")
for pizza in friend_pizza:
    print(pizza)