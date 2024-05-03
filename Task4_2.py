class Human:
    def __init__(self, name, city, birth_year):
        self.name = name
        self.city = city
        self.birth_year = birth_year

    def age(self):
        age = 2024 - self.birth_year
        return age

person = Human(str(input("Введите имя: ")), str(input("Введите город: ")), int(input("Введите Год рождения: ")))
print("Возраст:",person.age())
