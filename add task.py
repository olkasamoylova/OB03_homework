# базовый, родительский класс
class Animal:
    def __init__(self, name, type_of_animal):
        self.name = name
        self.type_of_animal = type_of_animal # задавать будем тип вводом

    def make_sound(self):
        return f"{self.name} издаёт звук."


class Zoo:
    def __init__(self):
        self.animals = []  # изначально пустой список для животных
        self.staff = []  # изначально пустой список для сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} принят на работу в зоопарк.")

    # блок для сохранения данных в файл
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            # сохраняем животных
            file.write("Animals:\n")
            for animal in self.animals:
                file.write(f"{animal.name},{animal.type_of_animal}\n")

            # сохраняем сотрудников
            file.write("Staff:\n")
            for staff in self.staff:
                file.write(f"{staff.name},{staff.__class__.__name__}\n")
        print(f"Информация о зоопарке сохранена в файл {filename}.")

    # загрузка данных из файла
    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Парсинг данных
        section = None
        for line in lines:
            line = line.strip()
            if line == "Animals:":
                section = "animals"
            elif line == "Staff:":
                section = "staff"
            elif line and section == "animals":
                name, type_of_animal = line.split(",")
                self.animals.append(Animal(name, type_of_animal))
            elif line and section == "staff":
                name, role = line.split(",")
                if role == "ZooKeeper":
                    self.staff.append(ZooKeeper(name))
                elif role == "Veterinarian":
                    self.staff.append(Veterinarian(name))
        print(f"Информация о зоопарке загружена из файла {filename}.")

    def show_zoo(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"{animal.name} ({animal.type_of_animal})")

        print("Сотрудники в зоопарке:")
        for staff in self.staff:
            print(f"{staff.name} - {staff.__class__.__name__}")


# классы и функции для сотрудников
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


# пример использования
zoo = Zoo()

# добавляем животных и сотрудников
zoo.add_animal(Animal("Воробей", "Bird"))
zoo.add_animal(Animal("Снежный барс", "Mammal"))
zoo.add_animal(Animal("Тритон", "Reptile"))

zoo.add_staff(ZooKeeper("Петр Савельев"))
zoo.add_staff(Veterinarian("Доктор Анна Зверинцева"))

# сохраняем данные о зоопарке в файл
zoo.save_to_file("zoo_data.txt")

# создаём новый зоопарк и загружаем данные из файла
new_zoo = Zoo()
new_zoo.load_from_file("zoo_data.txt")

# показываем загруженные данные
new_zoo.show_zoo()
