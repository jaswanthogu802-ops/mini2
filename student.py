def add_students():
    sid=input("enter student number:")
    if sid in students:
        print("students already exists!")
        return
    name=input("enter a name:")
    marks=input("enter marks:")
    students[sid]={"name":name,"marks":marks}
    print("student addedd successfully")
def view_students():
    if not students:
        print("no student found")
        return
print("\n------student list------")
for sid,details in students.items():
    print(f"sid:{sid},name:{details['name']},marks:{details['marks']}")
else:
    print("student not found")
def search_student():
    sid=input("enter sid number to search:")
    if sid in students:
        print(f"name:{students[sid]['name']},marks:{students[sid]['marks']}")
    else:
        print("student not found")
def update_student():
    sid=input("enter  sid number to update:")
    if sid in students:
        name=input("enter new name:")
        marks=input("enter marks:")
        students[sid]={"name":name,"marks":marks}
    else:
        print("student not found")
def delete_student():
    sid=input("enter sid number to delete:")
    if sid in students:
        del students[sid]
    print("student deleted successfully:")
while true:
    print("\n=======student mangement system========")
    print("1.add student")
    print("2.view student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("6.exit")
    choice=input("enter your choice 1-6:")
    if choice=='1':
        add_student()
    elif choice=='2':
        view_student()
    elif choice=='3':
        search_student()
    elif choice=='4':
        update_student()
    elif choice=='5':
        delete_student()
    elif choice=='6':
        print("existing program:")
        break
    else:
        print("invalid choicce!try again")
        
        
