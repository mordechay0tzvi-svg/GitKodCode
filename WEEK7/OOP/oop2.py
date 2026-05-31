class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

student1 = Student("roi",23, "uni")
student2 = Student("lenny",19, "uni")
student3 = Student("tora",20, "uni")
students_list = [student2,student3,student1]

class Building:
    def __init__(self):
        self.size = 0
        self.floors = 1
class School(Building):
    def __init__(self, name, size=0, floors=1):
        super().__init__()
        self.size = size
        self.floors = floors
        self.students = []
        self.name = name
    def get_average_age(self):
        if not self.students:
            return None
        return sum(stud.age for stud in self.students)/len(self.students)

uni = School("uni")
uni.students = students_list
print(uni.get_average_age())












