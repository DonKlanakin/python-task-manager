class Task:
    def __init__(self, task_id, title, description, due_date, completed=False):
        self.id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
            }