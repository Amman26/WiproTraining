from Oops_Concepts.student import student
class StudentGrade(student):
    def __init__(self, ccode, cname, ccity, rno, sname,m1,m2,m3,res, grd):
        super().__init__(ccode, cname, ccity, rno, sname, m1 , m2, m3)
        self.result = ''
        self.grade = None

    def calculate_result(self):
        avg = self.calculate_result()
        if avg >= 80.0:
            self.grade = 'A'
        elif avg >= 60.0:
            self.grade = 'B'
        elif avg >= 40.0:
            self.grade = 'C'
        else:
            self.grade = 'NA'