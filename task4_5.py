# чуть облегчим код, чтобы не вводить кучу параметров и сфокусироваться на общей логике
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Какой-то звук животного"

    def eat(self):
        return f"{self.name} ест."

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} чирикает"

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} рычит"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} шипит"


# Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
class Zoo:
    def __init__(self):
        self.animals = []  # изначально пустой список для животных
        self.staff = []    # изначально пустой список для сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} принят на работу в зоопарк.")

    def show_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name} - {animal.make_sound()}")

    def show_staff(self):
        print("Сотрудники в зоопарке:")
        for staff in self.staff:
            print(f"{staff.name} - {staff.__class__.__name__}") # как говорит чат - это обращение к классам ниже

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


