from storage import TaskStorage
from task import Task
from logger import Log

class TaskManager:
    @staticmethod
    def add_task(title, description, due_date):
        tasks = [Task(**task) for task in TaskStorage.load_tasks()]
        task_id = len(tasks) + 1
        task = Task(task_id, title, description, due_date)
        tasks.append(task)
        TaskStorage.save_tasks(tasks)
        print("Task added successfully!")

    @staticmethod
    def view_tasks():
        tasks = [Task(**task) for task in TaskStorage.load_tasks()]
        print("\nPending Tasks ::")
        for task in tasks:
            if not task.completed:
                print(f"ID: {task.id}, Title: {task.title}, Due: {task.due_date}")
        print("\nCompleted Tasks ::")
        for task in tasks:
            if task.completed:
                print(f"ID: {task.id}, Title: {task.title}, Due: {task.due_date}")

    @staticmethod
    def mark_task_complete(task_id):
        log_prefix = "[-TaskManager-] :: mark_task_complete"
        try:
            tasks = [Task(**task) for task in TaskStorage.load_tasks()]
            for task in tasks:
                if task.id == task_id:
                    task.completed = True
                    TaskStorage.save_tasks(tasks)
                    print("Task marked as complete!")
                    return
            print("Task not found!")
        except Exception as e:
            Log.error(log_prefix, "An error occurred.", e)

    @staticmethod
    def delete_task(task_id):
        log_prefix = "[-TaskManager-] :: delete_task"
        try:
            tasks = [Task(**task) for task in TaskStorage.load_tasks()]
            tasks = [task for task in tasks if task.id != task_id]
            TaskStorage.save_tasks(tasks)
            print("Task deleted successfully!")
            Log.info(log_prefix, "Task deleted successfully!")
        except Exception as e:
            Log.error(log_prefix, "An error occurred.", e)

    @staticmethod
    def search_tasks(query):
        log_prefix = "[-TaskManager-] :: search_tasks"
        try:
            tasks = [Task(**task) for task in TaskStorage.load_tasks()]
            results = [task for task in tasks if
                       query.lower() in task.title.lower() or query.lower() in task.description.lower() or query.lower() in task.due_date.lower()]
            if results:
                print("Search Results:")
                for task in results:
                    print(f"ID: {task.id}, Title: {task.title}, Due: {task.due_date}")
            else:
                print("No tasks found.")
        except Exception as e:
            Log.error(log_prefix, "An error occurred.", e)