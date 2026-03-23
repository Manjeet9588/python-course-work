fruit = ['apple','banana','mango','apple']
list = ['grapes','pinaple']

fruit.append('kiwi')
#print(fruit)
fruit.insert(1,'orange')
#print(fruit)
fruit.extend(list)
#print(fruit)
fruit.remove('apple')
print(fruit)

last_fruit = fruit.pop()
print(last_fruit)
print(fruit)

last_fruit = fruit.pop()
print(last_fruit)