class Student:
    def __init__(self, student_id=None, name=None, age=None, grade=None):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def update(self, name=None, age=None, grade=None):
        if name: self.name = name
        if age: self.age = age
        if grade: self.grade = grade
        if name or age or grade:
            print(f"Updated student: {self.name}, Age: {self.age}, Grade: {self.grade}")
        else:
            print("No updates made.")