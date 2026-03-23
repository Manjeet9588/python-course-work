''' Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
'''

glossary = {'print()': 'It is used to print output',
            'enumerate()': 'it is used to count the index in a list, dictionary',
            'input()': 'It is used for input by the user',
            'len()': 'It is used for length of variable',
            'map()': 'it used to store data in list'}
for key , value in sorted(glossary.items()):
    print(f"{key} : \n\t{value}\n")

glossary['type()'] = 'Return the data type of an object'
glossary['range()'] = 'Generate a sequence of a number'
glossary['max()'] = 'Give maximum value form iterable or from more then one argument'
glossary['min()'] = 'Give mimimum value form iterable or from more then one argument'
glossary['sum()'] = 'Give sum of value form iterable or from more then one argument'

print("\n\n\t\tFor new Dictionary\n\n")
for key , value in sorted(glossary.items()):
    print(f"{key} : \n\t{value}\n")
