# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"Ім'я - {self.name} та вік - {self.age}")
#
# student1 = Student("Влад", 22)
# student1.print_info()
# Завдання 2
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14159 * self.radius ** 2
#
#
# circle = Circle(5)
# area = circle.area()
#
# print(f"Площа кола з радіусом 5: {area}")
# Завдання 3
# class Book:
#
#     def __init__(self, title, author, genre):
#         self.title = title
#         self.author = author
#         self.genre = genre
#
#     def display_info(self):
#         print(f"Назва: {self.title}")
#         print(f"Автор: {self.author}")
#         print(f"Жанр: {self.genre}")
#
#
# book = Book("Володар перснів", "Дж. Р. Р. Толкін", "Фентезі")
# book.display_info()
# Завдання 4
# class Car:
#
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def start_engine(self):
#         print(f"Двигун автомобіля {self.brand} {self.model} {self.year} року випуску запущено!")
#
#
# car = Car("Toyota", "Supra", 2002)
# car.start_engine()
# Завдання 5
class BankAccount:

    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount
            print(f"Депозит на суму {amount} успішно здійснено!")
        else:
            print("Неможливо здійснити депозит на негативну суму!")

    def withdraw(self, amount):

        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Зняття коштів на суму {amount} успішно здійснено!")
        else:
            print("Недостатньо коштів на рахунку!")


account = BankAccount(1000, "Іван Петренко")

account.deposit(500)
account.withdraw(300)
account.withdraw(1000)

print(f"Баланс рахунку {account.owner}: {account.balance}")
