class Student:

    def __init__(self,name: str,age):
        self.name: str = name
        self.age = age
        self.grades = []

    def add_grade(self,notas: float):
        self.grades += notas


if __name__ == "__main__":
    estudiante_1: Student = Student("Carlos",18)
    estudiante_2: Student = Student("Luis",20)
    estudiante_3: Student = Student("Juan",16)

    estudiante_1.add_grade(4.5)
    estudiante_2.add_grade(3.0)
    estudiante_2.add_grade(2.5)

    print(grades)