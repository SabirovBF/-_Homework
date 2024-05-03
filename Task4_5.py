class Employee:
    def get_paid(self):
        if self.dol == "Менеджер":
            a = 5000
            print("Имя:", self.name, "Должность:", self.dol, "Зарплата:", a)
        elif self.dol == "Работник":
            a = 3000
            print("Имя:", self.name, "Должность:", self.dol, "Зарплата:", a)
        else:
            print("Такой должности нет")
class Manager(Employee):
    def __init__(self, name, dol):
        self.name = name
        self.dol = dol

class Worker(Employee):
    def __init__(self, name, dol):
        self.name = name
        self.dol = dol

manager = Manager(input("Введите имя: "), input("Введите должность: "))
worker = Worker(input("Введите имя: "), input("Введите должность: "))

print(manager.get_paid())
print(worker.get_paid())