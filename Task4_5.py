class Employee:
    def __init__(self, name, dol):
        self.name = name
        self.dol = dol

    def get_paid(self):
        if self.dol == "Менеджер":
            a = 5000
            return f'\nИмя: {self.name}  Должность: {self.dol}  Зарплата: {a}'
        elif self.dol == "Работник":
            a = 3000
            return f'\nИмя: {self.name}  Должность: {self.dol}  Зарплата: {a}'
class Manager(Employee):
    def get_paid(self):
        pass
class Worker(Employee):
    def get_paid(self):
        pass

manager = Employee(input("Введите имя: "), input("Введите должность: "))
worker = Employee(input("Введите имя: "), input("Введите должность: "))

print(manager.get_paid())
print(worker.get_paid())
