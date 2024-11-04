import datetime

class ActivityLogger:
    def _init_(self, log_file='activity_log.txt'):
        self.log_file = log_file  # Имя файла для журнала

    def create_entry(self):
        action = input("Введите действие, которое хотите записать: ")  # Запрос действия у пользователя
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получение текущего времени
        with open(self.log_file, 'a') as file:  # Открытие файла для добавления
            file.write(f"{timestamp} - {action}\n")  # Запись действия с временем
        print("Запись добавлена.")

    def read_entries(self):
        try:
            with open(self.log_file, 'r') as file:  # Открытие файла для чтения
                entries = file.readlines()  # Чтение всех записей
            if entries:
                print("Записи журнала активности:")
                for entry in entries:
                    print(entry.strip())  # Вывод каждой записи
            else:
                print("Журнал активности пуст.")
        except FileNotFoundError:
            print("Журнал активности еще не создан.")

    def clear_log(self):
        with open(self.log_file, 'w') as file:  # Открытие файла для записи (очистка)
            file.truncate()  # Очистка содержимого файла
        print("Журнал активности очищен.")