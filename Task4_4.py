class Chelovek:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"\nИмя: {self.name} \nВозраст: {self.age}"
person = Chelovek(input("Введите имя: "), input("Введите возраст: "))
print(person)
