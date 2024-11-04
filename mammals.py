class Mammals:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def run(self):
        print(f"{self.name} бежит!")

    def hunt(self):
        print(f"{self.name} охотится!")

    def nurture_young(self):
        print(f"{self.name} воспитывает потомство.")

    def communicate(self):
        print(f"{self.name} общается.")

    def eat(self):
        print(f"{self.name} ест {self.diet}.")


class Lion(Mammals):
    def __init__(self, name, age, mane_size, strength, pride_size):
        super().__init__(name, age, None, "Саванна", "мясо")
        self.mane_size = mane_size
        self.strength = strength
        self.pride_size = pride_size

    def make_sound(self):
        print(f"{self.name} рычит!")

    def hunt(self):
        print(f"{self.name} охотится в своей стае из {self.pride_size} львов.")


class Elephant(Mammals):
    def __init__(self, name, age, trunk_length, weight, tusk_size):
        super().__init__(name, age, weight, "Джунгли", "траву")
        self.trunk_length = trunk_length
        self.tusk_size = tusk_size

    def make_sound(self):
        print(f"{self.name} трубит!")

    def move(self):
        print(f"{self.name} передвигается с помощью своего хобота.")


class Kangaroo(Mammals):
    def __init__(self, name, age, jump_height, pouch_size, speed):
        super().__init__(name, age, None, "Австралия", "траву")
        self.jump_height = jump_height
        self.pouch_size = pouch_size
        self.speed = speed

    def make_sound(self):
        print(f"{self.name} издает звуки.")

    def run(self):
        print(f"{self.name} прыгает со скоростью {self.speed} км/ч.")


class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name               # Название шоу
        self.ticket_price = ticket_price         # Цена билета
        self.animal_performer = animal_performer # Животное-участник шоу
        self.tickets_sold = 0                   # Количество проданных билетов

    def perform_show(self):
      
        print(f"{self.animal_performer.name} выполняет трюк на шоу '{self.show_name}'!")

    def display_info(self):
        
        print(f"Шоу: {self.show_name}")
        print(f"Цена билета: {self.ticket_price} сом.")
        print(f"Животное-участник: {self.animal_performer.name}, вид: {type(self.animal_performer).__name__}, возраст: {self.animal_performer.age} лет")

    def sell_ticket(self, number_of_tickets):
       
        self.tickets_sold += number_of_tickets
        print(f"Продано {number_of_tickets} билетов на шоу '{self.show_name}'.")

    def calculate_revenue(self):
       
        revenue = self.tickets_sold * self.ticket_price
        print(f"Выручка от шоу '{self.show_name}': {revenue} сом.")
        return revenue

lion = Lion("Лев", 5, 0.5, 80, 10)
elephant = Elephant("Слон", 25, 2, 6000, 1.5)
kangaroo = Kangaroo("Кенгуру", 7, 3, 0.2, 60)

lion_show = ZooShow("Шоу льва", 500, lion)

lion_show.display_info()

lion_show.sell_ticket(100)

lion_show.perform_show()

lion_show.calculate_revenue()

elephant_show = ZooShow("Шоу слона", 700, elephant)

elephant_show.display_info()

elephant_show.sell_ticket(150)

elephant_show.perform_show()

elephant_show.calculate_revenue()

kangaroo_show = ZooShow("Шоу кенгуру", 300, kangaroo)

kangaroo_show.display_info()

kangaroo_show.sell_ticket(200)

kangaroo_show.perform_show()

kangaroo_show.calculate_revenue()
