class Student: 
    def __init__(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__dob = input("Enter student DOB: ")

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def set_stu_id(self, id):
        self.__id = id

    def set_stu_name(self, name):
        self.__name = name

    def set_stu_dob(self, dob):
        self.__dob = dob


class Course:
    def __init__(self):
        self.__c_id = input("Enter course ID: ")
        self.__c_name = input("Enter course name: ")

    def get_id(self):
        return self.__c_id
    
    def get_name(self):
        return self.__c_name
    
    def set_id(self, id):
        self.__c_id = id

    def set_name(self, name):
        self.__c_name = name


class School:
    def __init__(self):
        self.__marks = []
        self.__students = []
        self.__courses = []
        self.__num_students = 0
        self.__num_courses = 0 

    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses
    
    def getNumStu(self):
        return self.__num_students
    
    def getNumCou(self):
        return self.__num_courses

    def set_NumStu(self, num):
        self.__num_students = num 

    def set_NumCou(self, num):
        self.__num_courses = num 

    def add_student(self):
        num = self.getNumStu()
        for i in range (num):
            student = Student()
            self.__students.append(student)

    def add_courses(self):
        for i in range (self.getNumCou()):
            course = Course()
            self.__courses.append(course)

    def list_student(self):
        for i, student in enumerate(self.__students, 1):
            print(f"{i}. ID: {student.get_id()} - Name: {student.get_name()} - DOB: {student.get_dob()}")
        
    def list_course(self):
        for i, course in enumerate(self.__courses, 1):
            print(f"{i}. ID: {course.get_id()} - Name: {course.get_name()}")  

    def get_mark(self):
        num = int(input("Choose a course to edit: "))

        for student in self.__students:
            mark = input(float(f"Insert mark for {student.get_name()}: "))
            self.__marks.append('Course')


    

def main():
    school = School()
    
    while(True):
        print("=====================")
        print("List of actions:")
        print("1. Input number of students")
        print("2. Input information of students")
        print("3. Input number of courses")
        print("4. Input information of courses")
        print("5. List students")
        print("6. List courses")
        print("7. Select course and input marks.")
        print("8. List the marks of the chosen courses")
        print("0. Exit")

        option = int(input("Insert your choice:"))

        if option == 0:
            break
        elif option == 1:
            num = int(input("Enter the number of students: "))
            school.set_NumStu(num)
        elif option == 2:
            school.add_student()
        elif option == 3:
            num = int(input("Enter the number of courses: "))
            school.set_NumCou(num)
        elif option == 4:
            school.add_courses()
        elif option == 5:
            school.list_student()
        elif option == 6:
            school.list_course()
        elif option == 7:
            school.list_course()



# Call the main function
if __name__ == "__main__":
    main()