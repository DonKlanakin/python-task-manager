def main():
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
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                # format time
                # f() create a task
                print()
            except ValueError:
                print("Invalid date format!")
        elif choice == "2":
            # f() view tasks list
            print()
        elif choice == "3":
            # prompt for task id
            # f() mark task as complete
            print()
        elif choice == "4":
            # prompt for task id
            # f() delete task
            print()
        elif choice == "5":
            # prompt for keyword
            # f() search for tasks
            print()
        elif choice == "6":
            print("Exiting DK's Task Manager...")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()