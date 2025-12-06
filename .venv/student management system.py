class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name} | age: {self.age}"


class School:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("add student name: ").lower()
        age = int(input("add student age: "))
        new_student = Student(name, age)
        self.students.append(new_student)
        print("student added successfully\n")

    def remove_student(self):
        name = input("remove student name: ").lower()
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                print("student removed successfully\n")
                return
        print("student not found\n")

    def list_students(self):
        if not self.students:
            print("no students found\n")
        else:
            print("\n--- student list ---")
            for s in self.students:
                print(s)
            print()


def main():
    my_school = School()
    while True:
        print("=== student management system ===")
        print("1. add student")
        print("2. remove student")
        print("3. list students")
        print("4. exit")

        choice = input("enter option: ")

        if choice == "1":
            my_school.add_student()
        elif choice == "2":
            my_school.remove_student()
        elif choice == "3":
            my_school.list_students()
        elif choice == "4":
            print("goodbye!")
            break
        else:
            print("invalid choice, try again.\n")


main()
