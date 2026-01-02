from src.app import TodoApp

def main():
    app = TodoApp()

    while True:
        print("\n--- Todo App Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Complete")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            task = app.add_task(description)
            if task:
                print(f"Task added: ID {task.id}, Description: '{task.description}'")
            else:
                print("Error: Task description cannot be empty.")
        elif choice == '2':
            tasks = app.get_all_tasks()
            if not tasks:
                print("No tasks to display.")
            else:
                print("\n--- Your Tasks ---")
                for task in tasks:
                    status = "Completed" if task.completed else "Pending"
                    print(f"ID: {task.id}, Description: '{task.description}', Status: {status}")
        elif choice == '3':
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                new_description = input("Enter the new description: ")
                updated_task = app.update_task(task_id, new_description)
                if updated_task:
                    print(f"Task ID {updated_task.id} updated to: '{updated_task.description}'")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter the ID of the task to mark as complete: "))
                completed_task = app.mark_task_complete(task_id)
                if completed_task:
                    print(f"Task ID {completed_task.id} marked as complete.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")
        elif choice == '5':
            try:
                task_id = int(input("Enter the ID of the task to delete: "))
                if app.delete_task(task_id):
                    print(f"Task with ID {task_id} deleted.")
                else:
                    print(f"Error: Task with ID {task_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a numeric task ID.")
        elif choice == '6':
            print("Exiting Todo App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
