class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")


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
