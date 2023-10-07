# Klasa --- ma "pola" (fields) i "metody/funkcje"
class Robot:

    def __init__(self, name: str):
        print('uruchamiam konstruktor klasy A')
        self.name = name  # pole

    def foo(self):  # metoda
        name = 'Kadabra'
        return f'my name is {self.name}'

    def add(self, a: int, b: int):
        return a + b


class Mug:

    def __init__(self, color, capacity):
        self.capacity = capacity
        self.color = color
        self.content_amount = 0
        self.content_type = None

    def get_content_type(self):
        return self.content_type

    def get_content_amount(self):
        return self.content_amount

    def fill(self, content_type, content_amount):
        if self.content_type is not None and self.content_type != content_type:
            raise ValueError("Wrong type of liquid!")
        if content_amount > self.capacity:
            raise ValueError("Mug is overloaded!")
        self.content_amount = content_amount
        self.content_type = content_type

    def pour_out_liquid(self, requested_amount):
        if requested_amount > self.content_amount:
            raise ValueError("Can't overload the mug")
        self.content_amount -= requested_amount
        if self.content_amount == 0:
            self.content_type = None
        return self.content_type, requested_amount

# # tworzenie instancji
# a = Robot('Xiao')  # tworzenie instancji
#
# b = Robot('Li')  # tworzenie drugiej instancji
#
#
# print(a.foo())
# print(b.foo())


mug = Mug('black', 300)
mug.fill('coffe', 100)
mug.fill('water', 25)
print(mug.get_content_type())
print(mug.get_content_amount())

mug.pour_out_liquid(25)
print(mug.get_content_type())
print(mug.get_content_amount())

mug.pour_out_liquid(10)
print(mug.get_content_type())
print(mug.get_content_amount())
