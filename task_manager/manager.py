from storage import TaskStorage
from task import Task

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
        print("\nPending Tasks:")
        for task in tasks:
            if not task.completed:
                print(f"ID: {task.id}, Title: {task.title}, Due: {task.due_date}")
        print("\nCompleted Tasks:")
        for task in tasks:
            if task.completed:
                print(f"ID: {task.id}, Title: {task.title}, Due: {task.due_date}")