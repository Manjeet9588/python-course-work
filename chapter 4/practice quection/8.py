'''Check if character is vowel or consonant.'''

char = input("Enter a single char : ")

vowel = ['a','e','i','o','u','A','E','I','O','U']
if(len(char)==1 and char.isalpha()):
    if char in vowel:
        print("The given char is vowel")
    else:
        print("The given char is consonant")
else:
    print("Entered value is not a single char")