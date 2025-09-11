#Abstract class person
from abc import ABC,abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_role(self):
        pass
@abstractmethod
class Student(Person):
    def __init__(self,student_id,name,age):
        super().__init__(name,age)
        self.student_id=student_id
        self.enrolled_courses=[]

    def get_role(self):
        return 'Student'
    def get_enrolled_courses(self):
        print(self.enrolled_courses)
    def add_a_course(self, course_name):
        self.enrolled_courses.append(course_name)

stu1=Student(2, 'Mahesh', 35)
print(stu1.name)
stu1.get_enrolled_courses()
stu1.add_a_course('DPMS')
stu1.add_a_course('OOPS')
stu1.add_a_course('OS')
stu1.get_enrolled_courses()

class Teacher(Person):
    def __init__(self,teacher_id,name,age):
        super().__init__(name,age)
        self.teacher_id=teacher_id
        self.assign_courses=[]

    def get_role(self):
        return 'Teacher'
    def get_assign_courses(self):
        print(self.assign_courses)
    def add_a_course(self, course_name):
        self.assign_courses.append(course_name)

t1=Teacher(11, 'Ajay', 35)
print(t1.name)
t1.get_assign_courses()
t1.add_a_course('DPMS')
t1.add_a_course('OOPS')
t1.add_a_course('OS')

class Course:
    def __init__(self,course_name,course_code):
        self.course_name=course_name
        self.course_code=course_code
        self.teacher=None
        self.__students=[]

    def set_teacher(self,teacher):
        if self.teacher is None:
            self.teacher=teacher
        else:
             print(f"{self.course_name} already has a teacher assigned.")

    def enroll_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def course_info(self):
        students_names = [s.name for s in self.__students]
        teacher_name = self.teacher.name if self.teacher else "None"
        return {
            "Course": self.course_name,
            "Code": self.course_code,
            "Teacher": teacher_name,
            "Students": students_names
        }


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.__courses = []
        self.__teachers = []
        self.__students = []

    def add_course(self, course):
        self.__courses.append(course)

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def add_student(self, student):
        self.__students.append(student)

    def summary_info(self):
        return {
            "Department": self.department_name,
            "Courses": [c.course_name for c in self.__courses],
            "Teachers": [t.name for t in self.__teachers],
            "Students": [s.name for s in self.__students]
        }


class Administration:
    def __init__(self):
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def department_info(self):
        return [d.summary_info() for d in self.__departments]


if __name__ == "__main__":
    
    admin = Administration()

    
    cs_dept = Department("Computer Science")
    admin.add_department(cs_dept)

    
    ds = Course("Data Structures", "CS101")
    algo = Course("Algorithms", "CS102")
    cs_dept.add_course(ds)
    cs_dept.add_course(algo)

    
    alice = Teacher("Alice", 40, "T001")
    bob = Teacher("Bob", 45, "T002")
    cs_dept.add_teacher(alice)
    cs_dept.add_teacher(bob)


    alice.assign_to_course(ds)
    bob.assign_to_course(algo)

    
    john = Student("John", 20, "S001")
    jane = Student("Jane", 21, "S002")
    cs_dept.add_student(john)
    cs_dept.add_student(jane)

    
    john.enroll_in_course(ds)
    jane.enroll_in_course(algo)
    jane.enroll_in_course(ds)

    
    print("\nDepartment Info:")
    print(cs_dept.summary_info())

    
    print("\nCourse Info - Data Structures:")
    print(ds.course_info())

    print("\nCourse Info - Algorithms:")
    print(algo.course_info())

    
    print("\nAdministration Info:")
    print(admin.department_info())
       


            




 