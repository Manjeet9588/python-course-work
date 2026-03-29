'''Merge two dictionaries'''

from functions import get_dictionaries

dic_1 = get_dictionaries()

print("Enter your second dictonary")
dic_2 = get_dictionaries()

new_dic = dic_1 | dic_2
print(new_dic)