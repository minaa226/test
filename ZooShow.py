class Lion:
    def __init__(self, name, age, speed, weight, mane_size):
        self.name = name
        self.age = age
        self.speed = speed
        self.weight = weight
        self.mane_size = mane_size

    def make_sound(self):
        print(f"{self.name} рычит!")


class Elephant:
    def __init__(self, name, age, height, weight, tusk_length):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.tusk_length = tusk_length

    def make_sound(self):
        print(f"{self.name} трубит!")


class Kangaroo:
    def __init__(self, name, age, pouch_size, jump_height, speed):
        self.name = name
        self.age = age
        self.pouch_size = pouch_size
        self.jump_height = jump_height
        self.speed = speed

    def make_sound(self):
        print(f"{self.name} издает звуки!")


class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name
        self.ticket_price = ticket_price
        self.animal_performer = animal_performer
        self.tickets_sold = 0

    def perform_show(self):
        print(f"{self.animal_performer.name} выполняет трюк на шоу '{self.show_name}'!")
        self.animal_performer.make_sound()

    def display_info(self):
        print(f"{self.show_name} — Цена: {self.ticket_price} сом, Участник: {self.animal_performer.name}, Возраст: {self.animal_performer.age} лет")

    def sell_ticket(self, number_of_tickets):
        self.tickets_sold += number_of_tickets
        print(f"Продано {number_of_tickets} билетов")

    def calculate_revenue(self):
        return self.tickets_sold * self.ticket_price


# Примеры использования
lion_show = ZooShow("Шоу льва", 500, Lion("Лев", 5, 0.5, 80, 10))
elephant_show = ZooShow("Шоу слона", 700, Elephant("Слон", 25, 2, 6000, 1.5))
kangaroo_show = ZooShow("Шоу кенгуру", 300, Kangaroo("Кенгуру", 7, 3, 0.2, 60))

for show in [lion_show, elephant_show, kangaroo_show]:
    show.display_info()
    show.sell_ticket(100)
    show.perform_show()
    print(f"Выручка: {show.calculate_revenue()} сом\n")

