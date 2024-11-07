class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        self.lecturer_rating = 0

    def __str__(self):
        return f'Лектор: {self.name} {self.surname}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Эксперт: {self.name} {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress.append('Python')

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached.append('Python')

cool_reviewer = Reviewer('Expert', 'One')
cool_reviewer.courses_attached.append('Python')

cool_lecturer.rate_hw(best_student, 'Python', 10)
cool_lecturer.rate_hw(best_student, 'Python', 9)

print(best_student.grades)