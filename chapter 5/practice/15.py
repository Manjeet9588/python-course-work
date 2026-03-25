'''Check if character is vowel/consonant'''

char = input("Enter a alphabat char for check vowel/consonant : ")
vowel = 'aeiouAEIOU'
if len(char) != 1:
    print("Please enter only one char")
elif not char.isalpha():
    print("Please enter a valid alphabat a-z or A-Z")
elif char in vowel:
    print("The entered char is a vowel")
else:
    print("The entered char is consonant")