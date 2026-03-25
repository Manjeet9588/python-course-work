'''Compare 3 strings lexicographically'''
strings = [string for string in input("Enter your strings for compare seprated by space : ").split()]
strings = sorted(strings)

for n in range(len(strings)):
    if n < len(strings)-1:
        print(f"{strings[n]} <",end=" ")
    else:
        print(f"{strings[n]}")
