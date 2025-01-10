class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

student = Student("John Doe", 20, [90, 85, 88, 92])
student.display_details()
print("Average Grade:", student.average_grade())
