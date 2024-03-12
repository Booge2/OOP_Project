class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


person1 = Person("Іван Петренко", 25)
person2 = Person("Марія Іванова", 17)

print(f"{person1.name} - дорослий? {person1.is_adult()}")
print(f"{person2.name} - дорослий? {person2.is_adult()}")
