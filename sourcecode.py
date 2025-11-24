import json

# --- 1. Task Management Module ---
class Task:
    def __init__(self, title, description, due_date="N/A", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(data["title"], data["description"], data["due_date"], data["completed"])

tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    new_task = Task(title, description, due_date)
    tasks.append(new_task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    for i, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{i+1}. Title: {task.title}, Description: {task.description}, Due: {task.due_date}, Status: {status}")

def mark_task_complete():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to mark complete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num].completed = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# --- 2. Persistence Module ---
def save_tasks(filename="tasks.json"):
    with open(filename, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)
    print("Tasks saved.")

def load_tasks(filename="tasks.json"):
    global tasks
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            tasks = [Task.from_dict(item) for item in data]
        print("Tasks loaded.")
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
    except json.JSONDecodeError:
        print("Error loading tasks. JSON file might be corrupted.")
        tasks = []

# --- 3. User Interface (UI) Module ---
def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def main():
    load_tasks() # Load tasks on startup
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_complete()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
        elif choice == '6':
            load_tasks()
        elif choice == '7':
            save_tasks() # Save before exiting
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
