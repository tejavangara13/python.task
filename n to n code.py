#Abstracted class person

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass


class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.enrolled_courses = []

    def get_role(self):
        return "Student"

    def get_enrolled_courses(self):
        print(f"Enrolled Courses for {self.name}: {self.enrolled_courses}")

    def add_a_course(self, course_name):
        if course_name not in self.enrolled_courses:
            self.enrolled_courses.append(course_name)


class Teacher(Person):
    def __init__(self, teacher_id, name, age):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.assigned_courses = []

    def get_role(self):
        return "Teacher"

    def get_assigned_courses(self):
        print(f"Assigned Courses for {self.name}: {self.assigned_courses}")

    def add_a_course(self, course_name):
        if course_name not in self.assigned_courses: 
            self.assigned_courses.append(course_name)


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = None
        self.students = []

    def set_teacher(self, teacher):
        if self.teacher is None:  
            self.teacher = teacher
            teacher.add_a_course(self.course_name)

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_a_course(self.course_name)

    def get_course_info(self):
        print(f"\nCourse: {self.course_name} ({self.course_code})")
        print("Teacher:", self.teacher.name if self.teacher else "Not assigned")
        print("Students:", [stu.name for stu in self.students])


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []
        self.teachers = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def get_summary_info(self):
        print(f"\nDepartment: {self.department_name}")
        print("Courses:", [c.course_name for c in self.courses])
        print("Teachers:", [t.name for t in self.teachers])
        print("Students:", [s.name for s in self.students])


class Administration:
    def __init__(self):
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_department_info(self):
        for dept in self.departments:
            dept.get_summary_info()


if __name__ == "__main__":

    cs_dept = Department("Computer Science")

    c1 = Course("Data Structures", "CS101")
    c2 = Course("Algorithms", "CS102")

    t1 = Teacher("T001", "Alice", 40)
    t2 = Teacher("T002", "Bob", 38)


    s1 = Student("S001", "John", 20)
    s2 = Student("S002", "Jane", 21)

    c1.set_teacher(t1)
    c2.set_teacher(t2)

    c1.enroll_student(s1)
    c1.enroll_student(s2)
    c2.enroll_student(s2)

    cs_dept.add_course(c1)
    cs_dept.add_course(c2)
    cs_dept.add_teacher(t1)
    cs_dept.add_teacher(t2)
    cs_dept.add_student(s1)
    cs_dept.add_student(s2)

    admin = Administration()
    admin.add_department(cs_dept)

    c1.get_course_info()
    c2.get_course_info()
    admin.get_department_info()

    print("\n--- Student Details ---")
    print(f"Name: {s1.name}, ID: {s1.student_id}, Role: {s1.get_role()}")
    s1.get_enrolled_courses()
    print(f"Name: {s2.name}, ID: {s2.student_id}, Role: {s2.get_role()}")
    s2.get_enrolled_courses()

    print("\n--- Teacher Details ---")
    print(f"Name: {t1.name}, ID: {t1.teacher_id}, Role: {t1.get_role()}")
    t1.get_assigned_courses()
    print(f"Name: {t2.name}, ID: {t2.teacher_id}, Role: {t2.get_role()}")
    t2.get_assigned_courses()
