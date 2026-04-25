from Oops_Concepts.College import College
from Oops_Concepts.student import student
cc = int(input('C Code: '))
cn = input('C Name: ')
ci = input('City: ')
rno = int(input('Roll No: '))
sn = input('student Name: ')
m1 = int(input('M1: '))
m2 = int(input('M2: '))
m3 = int(input('M3: '))
'''project = College(ccode=cc, cname=cn, ccity =ci)

project.welcome_message()
project.display_college_details()
'''

project = student(ccode=cc, cname=cn, ccity=ci, rno=rno, sname=sn,m1=m1, m2=m2, m3=m3)
project.welcome_message()
project.display_college_details()
print(f'Roll No: {project.rollno} \t  Name: {project.stuname}'
      f'Total: {project.calculate_total()} \n Average:{project.calculate_average()}')