from students import get_students_list, save_data,delete_student,View_students_list

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