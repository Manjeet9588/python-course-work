'''Create student record system'''

import json
filename = 'students_list.json'

# to get list from data
def get_students_list():
    try:
        with open(filename) as file:
            students = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        students = {}
    return students


# for save current data to json file
def save_data(students):
    with open(filename, 'w') as file:
        json.dump(students,file,indent=4)
    

# to store new student name in students data
def add_new_student():
    students = get_students_list()
    while True:
        num = input("How many new students are there and 'q' for quit : ")
        if num.lower() == 'q':
            break
        if not num.isdigit():
            print("Enter a valid number or quit")
            continue
        num = int(num)
        for _ in range(num):
            stu_name = input("Enter student name : ").strip()
            stu_name = stu_name.title()
            if stu_name in students:
                print("This name is already exist: ")
                continue

            else:
                students[stu_name] = {}
                students[stu_name]['Name'] = stu_name
                students[stu_name]['Age'] = int(input("Enter student age : "))
                students[stu_name]['Class'] = input("Enter student class : ")
                students[stu_name]['Address'] = input("Enter student address : ")
                print(f"Student {stu_name} added successfully!")

        save_data(students) 
        print("Records updated successfully.")
        break

# to find student detail
def find_student():
    students = get_students_list()
    while True:
        stu_name = input("Enter student name or 'q' for quit : ").strip()
        stu_name = stu_name.title()
        if stu_name.lower() == 'q':
            break
        elif stu_name in students:
            print("Student Found")
            for name, details in students[stu_name].items():

                print(f"{name} : {details}")
            print()
            break
        else:
            print(f"Student {stu_name} not Found")
            break

# for view comlpete list
def View_students_list():
    students = get_students_list()
    count = 1
    for name, details in students.items():
        print(f"[{count}] {name} : ", end="")
        
        # Convert items to a list to get the length
        items = list(details.items())
        for i in range(len(items)):
            key, detail = items[i]
            # Print the data
            print(f"{key} : {detail}", end="")
            # print a comma only if it is NOT the last item
            if i < len(items) - 1:
                print(", ", end="")
        
        print() # New lin
        count +=1

# to update student information
def update_student():
    students = get_students_list()
    stu_name = input("Enter student name to update : ").strip()
    stu_name = stu_name.title()
    if stu_name in students:
        print(f"You are able to update {stu_name} details")
        while True:
            user_input = input(f"Do you want to update Name as well? (yes/no):  ")
            if user_input.lower() == 'yes':
                del students[stu_name]
                new_stu_name = input("Enter new Name : ").strip()
                new_stu_name = new_stu_name.title()
                students[new_stu_name] = {}
                
                students[new_stu_name]['Name'] = new_stu_name
                students[new_stu_name]['Age'] = int(input("Enter new Age : "))
                students[new_stu_name]['Class'] = input("Enter new Class : ")
                students[new_stu_name]['Address'] = input("Enter new Address : ")
                break

            elif user_input.lower() == 'no':

                students[stu_name]['Age'] = int(input("Enter student age for update : "))
                students[stu_name]['Class'] = input("Enter student class for update : ")
                students[stu_name]['Address'] = input("Enter student address for update : ")
                break

            else:
                print("Enter a valid input from 'yes' or 'no'")
        
        save_data(students)
        print(f"Student {new_stu_name} updated successfully!")
    
    else:
        print("Student not found.")

# for delete student information
def delete_student():
    students = get_students_list()
    while True:
        stu_name = input("Enter Student Name to delete (or 'q' to quit): ").strip()
        stu_name = stu_name.title()
        if stu_name.lower() == 'q':
            break
        elif stu_name in students:
            user = input("Are you sure you want to delete [Name]? (yes/no): ")
            if user.lower() == 'yes':
                del students[stu_name]
                print(f"Student {stu_name} deleted successfully!.")
            elif user.lower() == 'no':
                break
            else:
                print("Enter a valid input or 'q' for quit")
        else:
            print(f"Student not found.")


