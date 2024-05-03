class Matematic:
    def summa(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def umnojit(self, a, b):
        return a * b

    def delit(self, a, b):
        if b == 0:
            print("На ноль НЕЛЬЗЯ!")
        return a / b
f = Matematic()
print(f.summa(2,3))
print(f.minus(2,3))
print(f.umnojit(2,3))
print(f.delit(2,3))