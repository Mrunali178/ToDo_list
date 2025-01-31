# To-Do List Manager

# Initialize an empty list to store tasks
tasks = []

def display_menu():
    """Display the menu options to the user."""
    print("\nTo-Do List Manager")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove a Task")
    print("5. Exit")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return
    
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} - {status}")

def mark_task_completed():
    """Mark a specific task as completed."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def remove_task():
    """Remove a task from the list."""
    view_tasks()
    if not tasks:
        return
    
    try:
        task_number = int(input("Enter the task number to remove: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed successfully!")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Thank You")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
