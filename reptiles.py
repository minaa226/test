class Reptiles:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def crawl(self):
        print(f"{self.name} ползет.")

    def shed_skin(self):
        print(f"{self.name} сбрасывает кожу.")

    def bask_in_sun(self):
        print(f"{self.name} греется на солнце.")

    def lay_eggs(self):
        print(f"{self.name} откладывает яйца.")

    def eat(self):
        print(f"{self.name} ест {self.diet}.")


class Snake(Reptiles):
    def __init__(self, name, age, length, venomous, scales_type):
        super().__init__(name, age, None, "Лес", "Мясо")
        self.length = length
        self.venomous = venomous
        self.scales_type = scales_type

    def make_sound(self):
        print(f"{self.name} шипит.")

    def move(self):
        self.crawl()


class Lizard(Reptiles):
    def __init__(self, name, age, color, tail_length, diet):
        super().__init__(name, age, None, "Пустыня", diet)
        self.color = color
        self.tail_length = tail_length

    def make_sound(self):
        print(f"{self.name} издает тихий шорох.")

    def move(self):
        self.crawl()


class Turtle(Reptiles):
    def __init__(self, name, age, shell_size, speed, life_span):
        super().__init__(name, age, None, "Водоем", "Трава")
        self.shell_size = shell_size
        self.speed = speed
        self.life_span = life_span

    def make_sound(self):
        print(f"{self.name} издает тихий звук.")

    def move(self):
        print(f"{self.name} движется со скоростью {self.speed} км/ч.")


# Создаем объекты
snake = Snake("Кобра", 5, 2, True, "Гладкая")
snake.eat()
snake.shed_skin()
snake.make_sound()
snake.move()

lizard = Lizard("Геккон", 2, "Зеленый", 0.3, "Насекомое")
lizard.bask_in_sun()
lizard.move()

turtle = Turtle("Черепаха", 80, 1.2, 0.3, 100)
turtle.lay_eggs()
turtle.move()
