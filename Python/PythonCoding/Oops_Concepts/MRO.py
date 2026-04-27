# demoC.py

class B:
    def __init__(self, msg):
        self.msg = msg

    def display(self):
        print("Message:", self.msg)


class C(B):
    def __init__(self, n1, n2, msg):
        super().__init__(msg)
        self.n1 = n1
        self.n2 = n2

    def final(self):
        print(f"n1={self.n1}, n2={self.n2}, msg={self.msg}")
