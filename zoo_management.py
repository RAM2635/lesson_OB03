class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age


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
