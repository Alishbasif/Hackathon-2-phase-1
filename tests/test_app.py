from src.models import Task
from src.app import TodoApp

def test_task_creation():
    task = Task(id=1, description="Test Task", completed=False)
    assert task.id == 1
    assert task.description == "Test Task"
    assert task.completed is False

def test_app_initial_state():
    app = TodoApp()
    assert len(app.tasks) == 0
    assert app.next_id == 1

def test_add_task_success():
    app = TodoApp()
    task = app.add_task("New Task")
    assert task is not None
    assert task.id == 1
    assert task.description == "New Task"
    assert task.completed is False
    assert len(app.tasks) == 1
    assert app.next_id == 2

def test_add_task_empty_description():
    app = TodoApp()
    task = app.add_task("")
    assert task is None
    assert len(app.tasks) == 0
    assert app.next_id == 1

def test_get_all_tasks_multiple_tasks():
    app = TodoApp()
    app.add_task("Task 1")
    app.add_task("Task 2")
    tasks = app.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].description == "Task 1"
    assert tasks[1].description == "Task 2"

def test_get_all_tasks_empty():
    app = TodoApp()
    tasks = app.get_all_tasks()
    assert len(tasks) == 0

def test_update_task_success():
    app = TodoApp()
    task = app.add_task("Old description")
    updated_task = app.update_task(task.id, "New description")
    assert updated_task is not None
    assert updated_task.description == "New description"
    assert app.find_task_by_id(task.id).description == "New description"

def test_update_task_non_existent():
    app = TodoApp()
    updated_task = app.update_task(999, "New description")
    assert updated_task is None

def test_mark_task_complete_success():
    app = TodoApp()
    task = app.add_task("Task to complete")
    completed_task = app.mark_task_complete(task.id)
    assert completed_task is not None
    assert completed_task.completed is True
    assert app.find_task_by_id(task.id).completed is True

def test_mark_task_complete_non_existent():
    app = TodoApp()
    completed_task = app.mark_task_complete(999)
    assert completed_task is None

def test_delete_task_success():
    app = TodoApp()
    task = app.add_task("Task to delete")
    result = app.delete_task(task.id)
    assert result is True
    assert app.find_task_by_id(task.id) is None
    assert len(app.tasks) == 0

def test_delete_task_non_existent():
    app = TodoApp()
    result = app.delete_task(999)
    assert result is False
