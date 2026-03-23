'''Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.'''

info = {}

first_name = input("Enter your first name : ")
info['first_name'] = first_name
last_name = input("Enter your last name : ")
info['last_name'] = last_name
age = int(input("Enter your age : "))
info['age'] = age
city = input("Enter your city : ")
info['city'] = city
for keys,value in info.items():
    if isinstance(value, str):
        print(f"{keys.title()}: {value.title()}")
    else:
        print(f"{keys.title()}: {value}")
