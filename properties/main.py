class Person:
    def __init__(self, age):
        self.__age = age   # hidden attribute

    @property
    def age(self):
        return self.__age   # getter

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value   # setter with validation
        else:
            raise ValueError("Age cannot be negative")
        

p = Person(25)
print(p.age)   # looks like direct access, but goes through the getter

p.age = 30     # looks like direct assignment, but goes through the setter
print(p.age)

p.age = -5     # raises ValueError
