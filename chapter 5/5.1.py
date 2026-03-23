''' Write a series of conditional tests. Print a statement describing each 
test and your prediction for the results of each test. Your code should look 
something like this:    car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''

# Variables define 
tech_stack = 'MERN'
semester = 6
is_coding_fun = True
laptop = 'MacBook'
coding_hours = 5

# for true
print("For True\n")

print("1. Is tech_stack == 'MERN'? I predict True.")
print(tech_stack == 'MERN')

print("\n2. Is semester >= 4? I predict True.")
print(semester >= 4)

print("\n3. Is is_coding_fun == True? I predict True.")
print(is_coding_fun == True)

print("\n4. Is laptop != 'Windows'? I predict True.")
print(laptop != 'Windows')

print("\n5. Is coding_hours * 2 == 10? I predict True.")
print(coding_hours * 2 == 10)


# for false
print("\nFor False ")

print("\n6. Is tech_stack == 'mern'? I predict False.")
print(tech_stack == 'mern') 

print("\n7. Is semester == 8? I predict False.")
print(semester == 8)

print("\n8. Is laptop == 'Dell'? I predict False.")
print(laptop == 'Dell')

print("\n9. Is coding_hours < 2? I predict False.")
print(coding_hours < 2)

print("\n10. Is is_coding_fun == False? I predict False.")
print(is_coding_fun == False)