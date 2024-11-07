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
        self.grades = {}  

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

def average_student_grade(students, course_name):
    total_grades = []
    for student in students:
        if course_name in student.grades:
            total_grades.extend(student.grades[course_name])
    
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)

def average_lecturer_grade(lecturers, course_name):
    total_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades.extend(lecturer.grades[course_name])
    
    if not total_grades:
        return 0
    return sum(total_grades) / len(total_grades)

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress.append('Python')
student1.rate_lecturer(Lecturer('Some', 'Buddy'), 'Python', 9)
student1.rate_lecturer(Lecturer('Some', 'Buddy'), 'Python', 10)

student2 = Student('Anna', 'Smith', 'female')
student2.courses_in_progress.append('Python')
student2.rate_lecturer(Lecturer('Some', 'Buddy'), 'Python', 8)
student2.rate_lecturer(Lecturer('Another', 'Lecturer'), 'Python', 7)

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached.append('Python')
lecturer1.grades['Python'] = [9.5, 8.5]

lecturer2 = Lecturer('Another', 'Lecturer')
lecturer2.courses_attached.append('Python')
lecturer2.grades['Python'] = [8.0]

reviewer1 = Reviewer('Expert', 'One')
reviewer2 = Reviewer('Expert', 'Two')

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

average_student_python = average_student_grade([student1, student2], 'Python')
average_lecturer_python = average_lecturer_grade([lecturer1, lecturer2], 'Python')

print(f'\nСредний балл студентов по курсу Python: {average_student_python:.1f}')
print(f'Средний балл лекторов по курсу Python: {average_lecturer_python:.1f}')