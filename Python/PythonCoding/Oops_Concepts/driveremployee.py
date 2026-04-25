#driver
from oopconcepts.employeedetails import EmployeeDetails

eno = int(input("Enter no: "))
name = input('Emo name: ')
bp = float(input('basic pay:'))
employee = EmployeeDetails(empno = eno , ename = name, basicpay = bp)
print('emp no: ',employee.empno)
print('emp name: ',employee.ename)
print('emp no: ',employee.basic_pay)
print('emp no: ',employee.calculate_netsal())