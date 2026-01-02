from typing import List, Optional
from src.models import Task

class TodoApp:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str) -> Optional[Task]:
        if not description:
            return None
        task = Task(id=self.next_id, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, new_description: str) -> Optional[Task]:
        task = self.find_task_by_id(task_id)
        if task:
            task.description = new_description
            return task
        return None

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        task = self.find_task_by_id(task_id)
        if task:
            task.completed = True
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False
