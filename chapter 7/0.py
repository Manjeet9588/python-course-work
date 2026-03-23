poll = {'man':['nar','goa'], 'shubham': ['goa']}
palce = input("Enter place : ")
tem = poll['man']
tem.append(palce)
poll['man'] = tem
print(tem)
print(poll)