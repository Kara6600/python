from student import Student

class CourseGroup:
    def __init__(self, student, classmates):
        self.student = student            # основной студент (тип Student)
        self.classmates = classmates      # список студентов (тип list of Student)