from datetime import datetime
from json import JSONDecodeError
from manager import TaskManager
from logger import Log

def main():
    log_prefix = "[-main-]"
    while True:
        print("\nDK's Task Manager ::")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            Log.info(log_prefix, "Choice 1 selected")
            # prompt for input
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                # format time
                datetime.strptime(due_date, "%Y-%m-%d")
                # f() create a task
                TaskManager.add_task(title, description, due_date)
                
            except ValueError as e:
                Log.error(log_prefix, f"Invalid date format (Must be YYYY-MM-DD).", e)
            except Exception as e:
                Log.error(log_prefix, "An error occurred.", e)
        elif choice == "2":
            Log.info(log_prefix, "Choice 2 selected")
            try:
                print("\n[- View All Tasks -]")
                TaskManager.view_tasks()
            except JSONDecodeError as e:
                Log.error(log_prefix, f"JSON parsing failed or file is empty.", e)
            except Exception as e:
                Log.error(log_prefix, "An error occurred.", e)
        elif choice == "3":
            Log.info(log_prefix, "Choice 3 selected")
            # prompt for task id
            # f() mark task as complete
        elif choice == "4":
            Log.info(log_prefix, "Choice 4 selected")
            # prompt for task id
            task_id = int(input("Enter task ID to delete: "))
            # f() delete task
            TaskManager.delete_task(task_id)
        elif choice == "5":
            Log.info(log_prefix, "Choice 5 selected")
            # prompt for keyword
            keyword = input("Enter keyword or due date to search: ")
            # f() search for tasks
            TaskManager.search_tasks(keyword)
            print()
        elif choice == "6":
            Log.info(log_prefix, "Choice 6 selected")
            Log.info(log_prefix, "Exiting DK's Task Manager...")
            break
        else:
            Log.error(log_prefix, "Invalid input.")
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()