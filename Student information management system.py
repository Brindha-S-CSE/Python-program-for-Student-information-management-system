students={}
def add_student():
    roll=input("Enter Roll no:")
    name=input("Enter name:")
    dept=input("Enter Department:")
    students[roll]={"Name":name,"Department":dept}
    print("Student added successfully")
def view_students():
    if not students:
        print("No student records found")
        return
    print("\n---Students records---")
    for roll,data in student.items():
        print("Roll no:",roll,"|Name:",data["Name"],"|Department:",data["Department"])
def search_student():
    roll=input("Enter roll no to search:")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found")
def delete_student():
    roll=input("Enter roll no of delete:")
    if roll in students:
        del students[roll]
        print("Student deleted successfully")
    else:
        print("Student not found")
while True:
    print("\n 1.Add student")
    print("2.View students")
    print("3.Search student")
    print("4.Delete student")
    print("5.Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_students()
    elif choice=="3":
        search_student()
    elif choice=="4":
        delete_student()
    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice1")