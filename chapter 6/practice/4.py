'''Find key with max value'''

from functions import get_dictionaries

def max_value(dic):
    max_key = max(dic,key= dic.get)
    return f"{max_key} : {dic[max_key]}"


data = get_dictionaries()
max_value = max_value(data)
print(max_value)