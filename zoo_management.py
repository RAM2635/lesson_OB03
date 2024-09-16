import json


# Базовый класс Animal
class Animal:
    sounds = {
        'Bird': "чирикает",
        'Mammal': "рычит",
        'Reptile': "шипит"
    }

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        sound = self.sounds.get(type(self).__name__)
        if sound:
            print(f"{self.name} {sound}")
        else:
            raise NotImplementedError("Subclasses must implement this method")

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")

    def __str__(self):
        return f"{self.name}, Возраст: {self.age}, Тип: {type(self).__name__}"


# Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def eat(self):
        print(f"{self.name} ест червяков")

    def sleep(self):
        print(f"{self.name} спит на ветке")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def eat(self):
        print(f"{self.name} ест мясо")

    def sleep(self):
        print(f"{self.name} спит в логове")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def eat(self):
        print(f"{self.name} ест насекомых")

    def sleep(self):
        print(f"{self.name} спит в тени")


# Функция для полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Классы сотрудников
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, Должность: {self.position}"


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, "Мастер чистоты")

    def clean_animal(self, animal):
        print(f"{self.name} чистит {animal.name}")


# Класс зоопарка с использованием композиции
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, new_animal):
        self.animals.append(new_animal)

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    # Сохранение состояния зоопарка в файл
    def save_to_file(self, filename):
        zoo_data = {
            'animals': [
                {
                    'name': a.name,
                    'age': a.age,
                    'type': type(a).__name__,
                    'wing_span': getattr(a, 'wing_span', None),
                    'fur_color': getattr(a, 'fur_color', None),
                    'scale_type': getattr(a, 'scale_type', None)
                } for a in self.animals
            ],
            'employees': [{'name': e.name, 'position': e.position} for e in self.employees]
        }

        with open(filename, 'w') as file:
            json.dump(zoo_data, file)

    # Загрузка состояния зоопарка из файла
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                zoo_data = json.load(file)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
            return
        except json.JSONDecodeError:
            print("Ошибка при декодировании JSON.")
            return

        for a_data in zoo_data['animals']:
            if a_data['type'] == 'Bird':
                self.animals.append(Bird(a_data['name'], a_data['age'], a_data['wing_span']))
            elif a_data['type'] == 'Mammal':
                self.animals.append(Mammal(a_data['name'], a_data['age'], a_data['fur_color']))
            elif a_data['type'] == 'Reptile':
                self.animals.append(Reptile(a_data['name'], a_data['age'], a_data['scale_type']))

        for e_data in zoo_data['employees']:
            if e_data['position'] == 'Смотритель':
                self.employees.append(ZooKeeper(e_data['name']))
            elif e_data['position'] == 'Ветеринар':
                self.employees.append(Veterinarian(e_data['name']))
            elif e_data['position'] == 'Мастер чистоты':
                self.employees.append(Cleaner(e_data['name']))


# Пример использования
if __name__ == "__main__":
    zoo = Zoo()

    # Добавление животных
    zoo.add_animal(Bird("Попугай", 2, 1.5))
    zoo.add_animal(Mammal("Лев", 5, "рыжий"))
    zoo.add_animal(Reptile("Змея", 3, "чешуйчатая"))

    # Добавление сотрудников
    zoo.add_employee(ZooKeeper("Андрей"))
    zoo.add_employee(Veterinarian("Екатерина"))
    zoo.add_employee(Cleaner("Иван"))

    # Сохранение данных зоопарка в файл
    zoo.save_to_file("zoo_data.json")

    # Загружаем данные зоопарка из файла
    new_zoo = Zoo()
    new_zoo.load_from_file("zoo_data.json")

    # Проверка загрузки данных
    for animal in new_zoo.animals:
        print(animal)

    for employee in new_zoo.employees:
        print(employee)
