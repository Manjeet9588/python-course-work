'''You don’t have to limit the number of tests you create to 10. If you want 
to try more comparisons, write more tests and add them to conditional_tests.py. 
Have at least one True and one False result for each of the following:
•Tests for equality and inequality with strings
•Tests using the lower() function
•Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
•Tests using the and keyword and the or keyword
•Test whether an item is in a list
•Test whether an item is not in a list'''

# String equality / inequality
car = 'Audi'

print("String equality test:")
print(car == 'Audi')   
print(car != 'Audi')   

# lower() function tests
print("\nUsing lower():")
print(car.lower() == 'audi')
print(car.lower() == 'bmw') 

# Numerical tests
num = 5

print("\nNumerical tests:")
print(num == 5)  
print(num != 5)  
print(num > 3)   
print(num < 3)   
print(num >= 5)  
print(num <= 4)     

# and / or keyword tests
print("\nUsing and / or:")
print(num > 3 and num < 10)   
print(num > 10 and num < 20)  
print(num < 3 or num == 5)    
print(num < 3 or num > 10)    

# List membership tests
cars = ['audi', 'bmw', 'toyota', 'swift']

print("\nList membership tests:")
print('bmw' in cars)         
print('mercedes' in cars)    
print('audi' not in cars)    
print('kia' not in cars)     


