class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_courses = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade:.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Хранение оценок от студентов

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum([sum(grades) for grades in self.grades.values()])
        total_courses = sum([len(grades) for grades in self.grades.values()])
        return total_grades / total_courses if total_courses > 0 else 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade:.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')
best_student.finished_courses.append('Введение в программирование')

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached.append('Python')

cool_reviewer = Reviewer('Expert', 'One')
cool_reviewer.courses_attached.append('Python')

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

print(best_student)
print(cool_lecturer)
print(cool_reviewer)

print(best_student < Student('Another', 'Student', 'your_gender'))  # Пример сравнения студентов
print(cool_lecturer < Lecturer('Another', 'Lecturer'))  # Пример сравнения лекторов