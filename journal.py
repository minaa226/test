import datetime

class ActivityLogger:
    def __init__(self, log_file='activity_log.txt'):
        self.log_file = log_file

    def create_entry(self):
        action = input("Введите действие: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as file:
            file.write(f"[{timestamp}] {action}\n")
        print("Действие добавлено в журнал.")

    def read_entries(self):
        try:
            with open(self.log_file, 'r') as file:
                entries = file.readlines()
            if entries:
                print("Журнал активности:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("Журнал пусто.")
        except FileNotFoundError:
            print("")

    def clear_log(self):
        with open(self.log_file, 'w') as file:
            file.write("")
        print("очищать журнал.")

def main():
    logger = ActivityLogger()
    
    while True:
        print("\nВыберите действие:")
        print("1. Добавить запись")
        print("2. Прочитать все записи")
        print("3. Очищать журнал")
        print("4. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == '1':
            logger.create_entry()
        elif choice == '2':
            logger.read_entries()
        elif choice == '3':
            logger.clear_log()
        elif choice == '4':
            print("Выход .")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
