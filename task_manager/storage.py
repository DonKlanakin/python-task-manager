import os
import json
from logger import Log

dir_name = os.path.dirname(__file__)
TASKS_FILE = os.path.join(dir_name, "../data/tasks.json")

class TaskStorage:
    @staticmethod
    def load_tasks():
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        else:
            Log.debug("[-TaskStorage-]", "Tasks file not found.")
        return []

    @staticmethod
    def save_tasks(tasks):
        with open(TASKS_FILE, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
