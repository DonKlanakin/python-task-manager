from json import JSONDecodeError
from manager import TaskManager
from logger import Log

def main():
    logPrefix = "[-main-]"
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
            try:
                # format time
                # f() create a task
                Log.info(logPrefix, "Choice 1 selected")
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
            except ValueError:
                Log.error(logPrefix, "Invalid date format.")
        elif choice == "2":
            try:
                Log.info(logPrefix, "Choice 2 selected")
                print("\n[- View All Tasks -]")
                TaskManager.view_tasks()
            except JSONDecodeError:
                Log.error(logPrefix, "JSON parsing failed or file is empty.")
        elif choice == "3":
            # prompt for task id
            # f() mark task as complete
            Log.info(logPrefix, "Choice 3 selected")
        elif choice == "4":
            # prompt for task id
            # f() delete task
            Log.info(logPrefix, "Choice 4 selected")
        elif choice == "5":
            # prompt for keyword
            # f() search for tasks
            Log.info(logPrefix, "Choice 5 selected")
            print()
        elif choice == "6":
            Log.info(logPrefix, "Choice 6 selected")
            Log.info(logPrefix, "Exiting DK's Task Manager...")
            break
        else:
            Log.error(logPrefix, "Invalid input.")
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()