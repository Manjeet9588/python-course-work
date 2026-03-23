'''Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.'''

from collections import OrderedDict




glossary = OrderedDict()
glossary['print()']= 'It is used to print output'
glossary["loop"] = "repeat code"
glossary["list"] = "collection"
glossary["tuple"] = "immutable"

for word, meaning in glossary.items():
    print(word, meaning)