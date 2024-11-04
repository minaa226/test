import os

class ToDoList:
    def __init__(self, file_name='todo_list.txt'):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, 'r') as file:
                return [line.strip().split(" | ") for line in file]
        return []

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            for task, status in self.tasks:
                file.write(f"{task} | {status}\n")

    def add_task(self):
        task = input("Введит задачи  ")
        self.tasks.append([task, 'выполнить'])
        self.save_tasks()
        print("добавить задачу.")

    def mark_done(self):
        self.view_tasks()
        try:
            task_num = int(input("номер задачи  ")) - 1
            if 0 <= task_num < len(self.tasks):
                self.tasks[task_num][1] = 'Выполнена'
                self.save_tasks()
                print("Задача отмечена .")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Введите корректный номер.")

    def remove_done_tasks(self):
        self.tasks = [task for task in self.tasks if task[1] != 'Выполнена']
        self.save_tasks()
        print("Выполненные задачи удалены.")

    def view_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("\nСписок задач:")
            for i, (task, status) in enumerate(self.tasks, start=1):
                print(f"{i}. {task} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n список задач")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить выполненные задачи")
        print("4. Посмотреть все задачи")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.mark_done()
        elif choice == '3':
            todo_list.remove_done_tasks()
        elif choice == '4':
            todo_list.view_tasks()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
