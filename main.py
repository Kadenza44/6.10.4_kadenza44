class Volunteer:
    position = "Волонтер"

    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self):
        return f"Гость: {self.name} {self.surname}, из г. {self.city}, должность: {self.position}"


class Mentor(Volunteer):
    position = "Наставник"


class Student(Volunteer):
    position = "Студент"


class Tester(Volunteer):
    position = "Тестировщик"


mentor1 = Mentor("Иван", "Иванов", "Москва")
mentor2 = Mentor("Пётр", "Петров", "Кострома")

student1 = Student("Михаил", "Михайлович", "Кострома")
student2 = Student("Ольга", "Ольговна", "Москва")

tester1 = Tester("Виктория", "Викторовна", "Тверь")
tester2 = Tester("Константин", "Аркадьевич", "Сызрань")

guests = [mentor1, mentor2, student1, student2, tester1, tester2]

for people in guests:
    print(people)
