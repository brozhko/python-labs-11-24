class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__marks = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_student_id(self):
        return self.__student_id

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if isinstance(marks, list):
            self.__marks = marks

    def add_mark(self, mark):
        self.__marks.append(mark)

    def average_mark(self):
        if self.__marks:
            return sum(self.__marks) // len(self.__marks)
        return 0

    def __str__(self):
        return f"ID Студента: {self.__student_id}, Ім'я: {self.__name}, Середній бал: {self.average_mark()}"

    def __del__(self):
        print(f"Студента: {self.__name} видалено")


class Group:
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__students = []

    def get_group_name(self):
        return self.__group_name

    def set_group_name(self, group_name):
        self.__group_name = group_name

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)

    def ranking(self):
        return sorted(self.__students, key=lambda student: student.average_mark(), reverse=True)

    def sort(self):
        for student in self.ranking():
            print(student)


if __name__ == "__main__":
    group = Group("IoT-11")

    student1 = Student("Іван", 21)
    student1.add_mark(85)
    student1.add_mark(90)
    student1.add_mark(78)

    student2 = Student("Максим", 22)
    student2.add_mark(70)
    student2.add_mark(60)
    student2.add_mark(75)

    student3 = Student("Анна", 32)
    student3.add_mark(100)
    student3.add_mark(92)
    student3.add_mark(97)

    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    print("Рейтинг студентів:")
    group.sort()
