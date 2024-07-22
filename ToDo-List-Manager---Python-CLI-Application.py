import json
from datetime import datetime

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for index, (task, deadline) in enumerate(tasks.items(), start=1):
        print(f"{index}. {task} - Deadline: {deadline}")

def add_task(tasks):
    task = input("Enter task description: ")
    deadline_str = input("Enter deadline (YYYY-MM-DD): ")

    try:
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    tasks[task] = deadline.strftime('%Y-%m-%d')
    save_tasks(tasks)
    print("Task added successfully.")

def edit_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    task_index = int(input("Enter task number to edit: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    task_keys = list(tasks.keys())
    task_to_edit = task_keys[task_index]
    new_deadline_str = input(f"Enter new deadline for '{task_to_edit}' (YYYY-MM-DD): ")

    try:
        new_deadline = datetime.strptime(new_deadline_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    tasks[task_to_edit] = new_deadline.strftime('%Y-%m-%d')
    save_tasks(tasks)
    print("Task deadline updated successfully.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    task_index = int(input("Enter task number to delete: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
        return

    task_keys = list(tasks.keys())
    task_to_delete = task_keys[task_index]
    del tasks[task_to_delete]
    save_tasks(tasks)
    print("Task deleted successfully.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== ToDo List Manager =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task Deadline")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting ToDo List Manager.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == '__main__':
    main()
