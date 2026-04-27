from Oops_Concepts.formulamethods import FM


class Rectangle(FM):
    def __init__(self, l,b):
        self.length = l
        self.breath = b

    def calculate_area(self):
        return self.length * self.breath

    def caluclate_perimeter(self):
        return 4 * (self.length + self.breath)