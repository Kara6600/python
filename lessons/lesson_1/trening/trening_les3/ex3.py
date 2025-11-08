from student import Student
from course_group import CourseGroup

# создаем основного студента
main_student = Student("Иван", "Иванов", 20, 3)

# создаем сокурсников
classmate1 = Student("Петр", "Петров", 21, 3)
classmate2 = Student("Светлана", "Смирнова", 22, 3)
classmate3 = Student("Алексей", "Кузнецов", 20, 3)

# создаем группу
group = CourseGroup(main_student, [classmate1, classmate2, classmate3])

# формируем строку со списком сокурсников
classmates_names = ', '.join([f"{student.name} {student.last_name}" for student in group.classmates])

# вывод информации
print(f"{group.student.name} {group.student.last_name}, {group.student.age} лет, учится на курсе {group.student.course} вместе с: {classmates_names}")