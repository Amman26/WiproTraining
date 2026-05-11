'''2. Employee Management System
You are developing an employee management system for a company. Implement a class
called Employee with the following specifications:
The class should have private instance variables for employee ID, name, and salary.
Include a constructor to initialize these variables.
Implement getter and setter methods for each instance variable.
Implement a method to display employee information.
Implement a method to give a salary hike to an employee. The method should accept a
percentage value by which the salary will be increased.
Write a Python program to demonstrate the functionality of the Employee class by
creating instances, displaying employee information, giving salary hikes, and displaying
updated employee information.'''

class Employee:
    def __init__(self, eid, emp_name, emp_salary):
        self.__eid = eid
        self.__emp_name = emp_name
        self.__emp_salary = emp_salary

    # getters
    def get_details(self):
        return self.__eid, self.__emp_name, self.__emp_salary

    # setters
    def update_name(self, name):
        self.__emp_name = name

    def update_salary(self, salary):
        if salary >= 0:
            self.__emp_salary = salary
        else:
            print("Salary cannot be negative")

    # display
    def show(self):
        print("\nEmployee ID:", self.__eid)
        print("Employee Name:", self.__emp_name)
        print("Monthly Salary:", self.__emp_salary)

    # salary hike
    def increase_salary(self, percent):
        if percent > 0:
            self.__emp_salary += (self.__emp_salary * percent / 100)
            print("Hike applied successfully")
            print("Updated Salary:", self.__emp_salary)
        else:
            print("Enter valid percentage")

    # extra feature
    def yearly_salary(self):
        print("Annual Salary:", self.__emp_salary * 12)


# -------- main prog --------
print("***** Employee System *****")
eid = int(input("Enter ID: "))
name = input("Enter Name: ")
salary = float(input("Enter Salary: "))

e1 = Employee(eid, name, salary)

while True:
    print("\nChoose option:")
    print("1 - View Details")
    print("2 - Increase Salary")
    print("3 - Annual Salary")
    print("4 - Change Name")
    print("5 - Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        e1.show()
    elif ch == "2":
        p = float(input("Enter percentage: "))
        e1.increase_salary(p)
    elif ch == "3":
        e1.yearly_salary()
    elif ch == "4":
        new_name = input("Enter new name: ")
        e1.update_name(new_name)
        print("Name changed")
    elif ch == "5":
        print("Program ended")
        break
    else:
        print("Wrong input, try again")
