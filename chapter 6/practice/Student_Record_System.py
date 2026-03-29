'''----------------------Student Record System----------------------'''

import students

# For print on screen
message = '\n\n1. Add Student\n' \
'2. View All Student\n' \
'3. Find Student\n' \
'4. Update Student\n' \
'5. Delete Student\n' \
'6. Exist\n\n' \
'Enter your choice (1-6): '

while True:
    try: 
        print(f"{"="*60}\n\t\tSTUDENT RECORD SYSTEM\n{"="*60}")
        user_input = int(input(message))  # take input from user
    except ValueError:  # for wrong input
        print("Enter a valid choice \n")
    
    else:
        if user_input == 1:     # for choice 1 (Add student)
            print(f"{"-"*60}\n\t\tADD NEW STUDENT\n{"="*60}")
            students.add_new_student()
        
        elif user_input == 2:   # for choice 2 (View all student)
            print(f"{"-"*60}\n\t\tALL STUDENTS LIST\n{"="*60}")
            students.View_students_list()
            a = input("\nPress Enter to return to main menu\n")
            if a:
                continue
            else:
                continue

        elif user_input == 3:   # for choice 3 (find student)
            print(f"{"-"*60}\n\t\tFIND STUDENT\n{"="*60}")
            students.find_student()

        elif user_input == 4:   # for choice 4 (update student)
            print(f"{"-"*60}\n\t\t UPDATE STUDENT\n{"="*60}")
            students.update_student()

        elif user_input == 5:   # for choice 5 (update student)
            print(f"{"-"*60}\n\t\tDELETE STUDENT\n{"="*60}")
            students.delete_student()

        elif user_input == 6:   # for choice 6 (Exist)
            print(f"{"-"*60}\n\t\tEXIT STUDENT SYSTEM\n{"="*60}")
            print(f"\nThank you for using the Student Record System!\n")
            break

        else:   #For another number
            print("Enter a valid choice")
