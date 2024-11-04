import datetime

class Calculator:
    def __init__(self, history_file='history.txt'):
        self.history_file = history_file

    def log(self, expression, result):
        with open(self.history_file, 'a') as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {expression} = {result}\n")

    def add(self, a, b):
        result = a + b
        self.log(f"{a} + {b}", result)
        return result

    def subtract(self, a, b):
        result = a - b
        self.log(f"{a} - {b}", result)
        return result

    def multiply(self, a, b):
        result = a * b
        self.log(f"{a} * {b}", result)
        return result

    def divide(self, a, b):
        if b == 0:
            print("Ошибка: деление на ноль")
            return None
        result = a / b
        self.log(f"{a} / {b}", result)
        return result

    def show_history(self):
        try:
            with open(self.history_file, 'r') as file:
                print("История вычислений:\n" + file.read())
        except FileNotFoundError:
            print("История пуста.")

def main():
    calc = Calculator()

    while True:
        print("\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. История\n6. Выход")
        choice = input("Выберите действие: ")

        if choice in ['1', '2', '3', '4']:
            a = float(input("Первое число: "))
            b = float(input("Второе число: "))
            if choice == '1':
                print("Результат:", calc.add(a, b))
            elif choice == '2':
                print("Результат:", calc.subtract(a, b))
            elif choice == '3':
                print("Результат:", calc.multiply(a, b))
            elif choice == '4':
                result = calc.divide(a, b)
                if result is not None:
                    print("Результат:", result)
        elif choice == '5':
            calc.show_history()
        elif choice == '6':
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
