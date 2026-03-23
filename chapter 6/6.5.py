'''Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary.'''

rivers = {'nile': 'egypt','amazon': 'brazil','yangtze':'china'}

for key , value in sorted(rivers.items()):
    print(f"The {key.title()} runs through {value.title()}")

print("\nAll the rivers are :")
for river in sorted(rivers.keys()):
    print(f"\t{river.title()}")

print("\nAll the country are :")
for country in sorted(rivers.values()):
    print(f"\t{country.title()}")
