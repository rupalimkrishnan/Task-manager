import json

TASKS_FILE = "tasks.json"

tasks = []


def load_tasks():
    """Load tasks from JSON file into memory."""
    global tasks
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    """Save current tasks list to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    """Add a new task."""
    title = input("Enter a task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return

    new_id = tasks[-1]["id"] + 1 if tasks else 1

    task = {
        "id": new_id,
        "title": title,
        "status": "pending"
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")



def list_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    print("Your tasks:")
    for task in tasks:
        status = "✔" if task["status"] == "done" else "✗"
        print(f'{task["id"]}. {task["title"]} [{status}]')



def delete_task():
    """Delete a task by ID."""
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    try:
        task_id = int(input("Enter task ID to delete: "))
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                save_tasks()
                print(f'Deleted task: {task["title"]}')
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main menu loop."""
    load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
