tasks = []

def add_task(task):
    tasks.append(task)
    print("Task Added: ", task)

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(i + 1, task)

def delete_task(index):
    index = index - 1
    del tasks[index]
    print("Task Deleted")

def main_menu():
    print("To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        index = int(input("Enter task index: "))
        delete_task(index)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")

