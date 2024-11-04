  # Базовый класс Animals
class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print(f"{self.name} is running!")

    def communicate(self):
        print(f"{self.name} is communicating!")


# Класс Mammals наследует от Animals
class Mammals(Animals):
    def nurture_young(self):
        print(f"{self.name} is nurturing its young!")

    def hunt(self):
        print(f"{self.name} is hunting!")


# Объект Лев
class Lion(Mammals):
    def __init__(self, name, age, mane_size, strength, pride_size):
        super().__init__(name, age)
        self.mane_size = mane_size
        self.strength = strength
        self.pride_size = pride_size

    def roar(self):
        print(f"{self.name} is roaring loudly!")


# Объект Слон
class Elephant(Mammals):
    def __init__(self, name, age, trunk_length, weight, tusk_size):
        super().__init__(name, age)
        self.trunk_length = trunk_length
        self.weight = weight
        self.tusk_size = tusk_size

    def trumpet(self):
        print(f"{self.name} is trumpeting loudly!")


# Объект Кенгуру
class Kangaroo(Mammals):
    def __init__(self, name, age, jump_height, pouch_size, speed):
        super().__init__(name, age)
        self.jump_height = jump_height
        self.pouch_size = pouch_size
        self.speed = speed

    def jump(self):
        print(f"{self.name} is jumping {self.jump_height} meters high!")


# Примеры создания объектов
simba = Lion(name="Simba", age=5, mane_size=20, strength=90, pride_size=15)
dumbo = Elephant(name="Dumbo", age=10, trunk_length=150, weight=5000, tusk_size=80)
jack = Kangaroo(name="Jack", age=3, jump_height=2, pouch_size=5, speed=60)

# Вызов методов
simba.run()
simba.hunt()
simba.roar()

dumbo.run()
dumbo.communicate()
dumbo.trumpet()

jack.run()
jack.jump()
jack.nurture_young()
