import time
FILE_NAME = 'students.txt'

def clr_scr():
    import os 
    os.system('cls')
# def wait(sec):
#     time.sleep(sec)
wait = time.sleep
def write_student_to_file(student_name, file_name):
    with open(file_name, 'a') as f1:
        f1.write(f"{student_name.capitalize()},")

def read_students(file_name):
    with open(file_name, 'r') as f2:
        students =  f2.read() # read method return type is string
        return students.split(",")
    
def display_students(students):
    # print(students)
    if len(students) > 0:
        for student in students:
            print(student)
    else:
        print("No students added yet !!!")

def main_menu():
    clr_scr()
    print("Welcome !!!")
    students = read_students(FILE_NAME)
    students.remove('')
    choice = input("""
    0. Exit
    1. Show all students
    2. Add Student                      
>""")
    # exception handling
    # Here, when the input is being converted to integer for comparison,
    # it might throw a 'ValueError' if the user enters a string value by mistake

    try: # this 'try' block provides the block of code with tendency to throw exception
        choice = int(choice)
        # this step might throw error
    except: # the 'except' block provides the code to execute in case of exception
        print("Please check your input")
        wait(2)
        return main_menu()
    finally: # this 'finally' block executes regardless 
        print(f"Your input was {choice}")
        wait(2)
    clr_scr()
    match choice: 
        case 0:
            return 0
        case 1:
            clr_scr()
            display_students(students)
            wait(2)
            input("\nPress Enter to continue...")
            
            return main_menu()
        case 2:
            clr_scr()
            student = input("Enter student name : ")
            if student in students:
                print(f"Student already exists by name {student}")
            else:
                write_student_to_file(student, FILE_NAME)
                clr_scr()
                print(f"Student {student.capitalize()} added !!!")
                wait(3)
            return main_menu()
        case _:
            print("Invalid input...")
            wait(2)
            return main_menu()
main_menu()