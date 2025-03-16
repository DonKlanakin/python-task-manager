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
    def delete_task(task_id):
        log_prefix = "[-TaskManager-] :: delete_task"
        try:
            tasks = [Task(**task) for task in TaskStorage.load_tasks()]
            tasks = [task for task in tasks if task.id != task_id]
            TaskStorage.save_tasks(tasks)
            print("Task deleted successfully!")
        except Exception as e:
            Log.error(log_prefix, "An error occurred.", e)