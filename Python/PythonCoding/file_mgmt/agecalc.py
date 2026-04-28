from file_mgmt.exception import AgeException


class Agecalc:
    def voting_age_check(self,age):
        if age < 18:
            raise AgeException("Not Eligible to vote")
        else:
            return True


    def pension_age_check(self,age):
        if age < 60:
            raise AgeException('NOT eligible to pension')