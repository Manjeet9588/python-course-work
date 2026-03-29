def get_dictionaries():
    print("'q' for quit any time")
    dictionary = {}
    while True:
        user_input = input("Enter key and value seprated by ',' : ")
        if user_input.lower() == 'q':
            break
        if ',' not in user_input:
            print("Error: Pleause use comma")
            continue

        key,value = user_input.split(',',1)
        dictionary[key.strip()] = value.strip()
    return dictionary


def invert_dictionary(dic):
    rev_dic = {}
    for key,value in dic.items():
        rev_dic[value] = key
    return rev_dic