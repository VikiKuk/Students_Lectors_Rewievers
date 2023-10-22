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
        if (isinstance(lecturer, Lecturer)
                and course in lecturer.courses_attached
                and course in self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _get_avg_grades(self):
        student_avg_grades = avg_grades(self.grades)
        return student_avg_grades

    def __gt__(self, other):
       return compare_gt(self, other)

    def __str__(self):
        result = ('Имя студента: ' + self.name + '\n' + 'Фамилия студента: ' + self.surname + '\n' +
                  'Средняя оценка за домашние задания: ' + str(self._get_avg_grades()) +'\n'+
                  'Курсы в процессе изучения: ' + ", ".join(self.courses_in_progress) +'\n'+
                  'Завершенные курсы: ' + (", ".join(self.finished_courses) if len(self.finished_courses) > 0 else 'Нет оконченных курсов') +'\n')
        return result

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _get_avg_grades(self):
        lecturer_avg_grades = avg_grades(self.grades)
        return lecturer_avg_grades

    def __gt__(self, other):
       return compare_gt(self, other)

    def __str__(self):
        result = ('Имя лектора: ' + self.name + '\n' + 'Фамилия лектора: ' + self.surname + '\n' +
                  'Средняя оценка за лекции: ' + str(self._get_avg_grades()) + '\n')
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = 'Имя ревьювера: ' + self.name + '\n' + 'Фамилия ревьювера: ' + self.surname + '\n'
        return result

def avg_grades(grades):
    sum_grade = 0
    n = 0
    for grade in grades.values():
        for temp in grade:
            sum_grade += temp
            n += 1
    if n != 0:
        return sum_grade/n
    else:
        return 'Отсутствуют оценки'


def compare_gt (left, right):
    n = avg_grades(left.grades)
    m = avg_grades(right.grades)
    if (not isinstance(n, str) and not isinstance(m, str)):
        return n > m
    elif not isinstance(n, str):
        return True
    else:
        return False

if __name__ == '__main__':

    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    best_student.courses_in_progress += ['Java']
    best_student2 = Student('Ivan', 'Carevich', 'your_gender')
    best_student2.courses_in_progress += ['Java']
    best_student2.finished_courses += ['SQL', 'Cabol']

    cool_mentor = Mentor('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']

    reviewers = Reviewer('Name Reviewer', 'Surname Reviewer')
    reviewers.courses_attached += ['Python']
    reviewers.courses_attached += ['Java']

    reviewers.rate_hw(best_student, 'Python', 5)
    reviewers.rate_hw(best_student, 'Python', 3)
    reviewers.rate_hw(best_student, 'Python', 1)
    reviewers.rate_hw(best_student, 'Java', 10)

    lecturer1 = Lecturer('Teacher1', 'Doe')
    lecturer1.courses_attached = ['Python', 'Java']
    lecturer2 = Lecturer('Teacher2', 'Joe')
    lecturer2.courses_attached += ['SQL', 'Python']


    best_student.rate_lecturer(lecturer1, 'Python', 3)
    best_student2.rate_lecturer(lecturer1, 'Java', 10)
    best_student.rate_lecturer(lecturer2, 'Python', 10)


    print(reviewers)
    print(lecturer1)
    print(lecturer2)
    print(best_student)
    print(best_student2)

    if best_student > best_student2:
        print('Средняя оценка ' + best_student.name + ' ' + best_student.surname + ' выше, чем ' + best_student2.name + ' ' + best_student2.surname)
    else:
        print('Средняя оценка ' + best_student2.name + ' ' + best_student2.surname + ' выше, чем ' + best_student.name + ' ' + best_student.surname)

    if lecturer1 > lecturer2:
        print('Средняя оценка ' + lecturer1.name + ' ' + lecturer1.surname + ' выше, чем ' + lecturer2.name + ' ' + lecturer2.surname)
    else:
        print('Средняя оценка ' + lecturer2.name + ' ' + lecturer2.surname + ' выше, чем ' + lecturer1.name + ' ' + lecturer1.surname)
