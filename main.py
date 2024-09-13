# Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Живое существо издает звук"

    def eat(self):
        return f"{self.name} с аппетитом ест."

# Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют
# от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)  # от Animal наследуем
        self.wing_span = wing_span  # атрибут "размах крыльев" для птиц

    def make_sound(self):
        return f"{self.name} чирикает"


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return f"{self.name} рычит"


class Reptile(Animal):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.length = length

    def make_sound(self):
        return f"{self.name} шипит"

# Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и
# вызывает метод `make_sound()` для каждого животного.

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

bird1 = Bird("Воробей", 3, 1.0)
mammal1 = Mammal("Лев", 5, "Золотой")
reptile1 = Reptile("Питон", 2, 6)

animals = [bird1, mammal1, reptile1]
animal_sound(animals)
