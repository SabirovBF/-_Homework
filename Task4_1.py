class Base_Figur:
    def get_info(self):
        print(f'Площадь: {self.square}; Периметр: {self.perimetr}')
class Rect(Base_Figur):
    def __init__(self,a,b):
        self.square = a * b
        self.perimetr = 2 * a + 2 * b
c = Rect(int(input("Введите высоту: ")),int(input("Введите ширину: ")))
c.get_info()