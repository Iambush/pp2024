def get_Numbers_Of_Student():
    num_sudents = int(input("Insert the number of student: "))
    return num_sudents

def get_Information_Of_Student():

    list_students = []
    temp = get_Numbers_Of_Student()

    if (temp == 0):
        print("There are 0 student.")
    else:
        for temp in range (temp):

            id = input("Student Id: ")
            name = input("Student Name: ")
            dob = input("Student DoB: ")
            print("===========================")

            info_student = {'id':id, 'name':name, 'dob':dob}

            list_students.append(info_student)
            #add info 1 student to the list
        return list_students

def get_Number_Of_Courses():
    num_courses = int(input("Insert number of courses: "))
    return num_courses

def get_Course_Information():
    list_courses = []
    temp = get_Number_Of_Courses()

    for temp in range(temp):
        id = input("Course ID: ")
        name = input("Course name: ")
        print("===========================")

        info_course = {'id':id, 'name':name}

        list_courses.append(info_course)
        #add info 1 course to the list
    return list_courses


def main():
    courses = []
    students = []
    num_students = 0
    num_courses = 0
    
    while(True):
        print("1. Input number of students")
        print("2. Input information of students")
        print("3. Input number of courses")
        print("4. Input information of courses")
        print("5. List students")
        print("6. List courses")
        print("")
        print("")
        print("0. Exit")
        

get_Information_Of_Student()
get_Course_Information()

