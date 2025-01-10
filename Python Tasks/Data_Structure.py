students = {}

def add_student(name, age, grades):
    students[name] = {"age": age, "grades": grades}

def view_students():
    for name, info in students.items():
        print("Name:", name, "| Age:", info["age"], "| Grades:", info["grades"])

def remove_student(name):
    if name in students:
        del students[name]
    else:
        print("Student not found.")

add_student("Shanks", 20, [80, 90, 85])
add_student("Luffy", 22, [78, 82, 88])
print("Student list:")
view_students()
print("Removing Nitin...")
remove_student("Nitin")
print("Updated student list:")
view_students()