'''Convert minutes into hours and remaining minutes.'''
time = int(input("Enter minutes for convert into hours : "))
converted_hours = time//60
left_minutes = time%60
print(f"The conversion of minutes into hours is {converted_hours} hours and {left_minutes} minutes")
