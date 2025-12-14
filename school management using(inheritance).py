class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def __str__(self):
        return f"firstname:{self.firstname}|lastname:{self.lastname}|age:{self.age}"
class Student(Person):
    def __init__(self,firstname,lastname,age,course,id_card):
        super().__init__(firstname,lastname,age)
        self.course=course
        self.id_card=id_card
    def  __str__(self):
        return f"firstname:{self.firstname}|lastname:{self.lastname}|age:{self.age}|course:{self.course}|id_card:{self.id_card}"

class Teacher(Person):
    def __init__(self,firstname,lastname,age,subject,salary):
        super().__init__(firstname,lastname,age)
        self.subject=subject
        self.salary=salary
    def __str__(self):
        return f"firstname:{self.firstname}|lastname:{self.lastname}|age:{self.age}|subject:{self.subject}|salary:{self.salary}"

class School:
    def __init__(self):
        self.students=[]
        self.teachers=[]

    def add_students(self):
        firstname=input("enter first name:").lower()
        lastname=input("enter last name:").lower()
        age=int(input("enter age:"))
        course=input("enter course:").lower()
        id_card=int(input("enter identification number"))
        t=Student(firstname,lastname,age,course,id_card)
        self.students.append(t)
        print("students added successfully.\n")


    def remove_students(self):
        id_card=input("enter students identification number").lower()
        for student in self.students:
            if id_card ==  self.students:
                self.students.remove(student)
                print("student removed successfully\n")
                return

            else:
                print("enter valid names.\n")


    def show_students(self):
        if not self.students:
            print("no students found.\n")

        else:
            for student in self.students:
                print(student)

    def add_teachers(self):
        firstname=input("enter first name:").lower()
        lastname=input("enter last name:").lower()
        age=int(input("enter age:"))
        subject=input("enter subject:").lower()
        salary=int(input("enter salary:"))
        x=Teacher(firstname,lastname,age,subject,salary)
        self.teachers.append(x)
        print("teacher added successfully")


    def remove_teachers(self):
        subject=input("enter teacher subject").lower()
        for teacher in self.teachers:
            if subject == self.teachers:
                self.teachers.remove(teacher)
                print("teacher removed successfully\n")
                return




    def show_teachers(self):
        if not self.teachers:
            print("no teachers found.\n")

        else:
            print("\n show teachers\n")
            for teacher in self.teachers:
                print(teacher)
            print()
def main():
    my_school=School()
    while True:
        print("\n===School Management System===\n")
        print("1.add student")
        print("2.remove students")
        print("3.show students")
        print("4.add teachers")
        print("5.remove teachers")
        print("6.show teachers")
        print("7.exit")

        option=input("enter option:")
        if option=="1":
            my_school.add_students()

        elif option=="2":
            my_school.remove_students()

        elif option=="3":
            my_school.show_students()

        elif option=="4":
            my_school.add_teachers()

        elif option=="5":
            my_school.remove_teachers()

        elif option=="6":
            my_school.show_teachers()

        elif option=="7":
            print("exit")
            break
        else:
            print("enter valid option")

main()