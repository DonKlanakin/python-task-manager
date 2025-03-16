import os
import json

TASKS_FILE = "data/tasks.json"

class TaskStorage:
    @staticmethod
    def load_tasks():
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        return []

    @staticmethod
    def save_tasks(tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
