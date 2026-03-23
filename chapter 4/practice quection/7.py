'''Grade calculator (marks → A/B/C/D).'''

math = int(input("Enter your math marks : "))
physic = int(input("Enter your physic marks : "))
chemistry = int(input("Enter your chemistry marks : "))

average = (math + physic + chemistry)/3

if(average>=90):
    print(f"Your grade is A and your percentage is {average}")
elif(75<=average>90):
    print(f"Your grade is B and your percentage is {average}")
elif(60<=average>75):
    print(f"Your grade is C and your percentage is {average}")
elif(40<=average>60):
    print(f"Your grade is D and your percentage is {average}")
else:
    print("Your are fail")