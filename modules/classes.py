import modules.mini_db as db

class Task:
    def __init__(self, name, is_completed=False, priority=int):
        self.name = name
        self.is_completed = is_completed
        self.priority = priority
    
    def get_task(self):
        return self

class ToDoList:
    def __init__(self, name, tasks=list(), is_completed=False,
                priority=0, category=str):
        self.name = name
        self.tasks = tasks
        self.is_completed = is_completed
        db.the_ref.append(self)

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            print('Please provide a valid task')

    def list_tasks(self):
        if len(self.tasks) > 0:
            for task in self.tasks:
                print(task)
        else:
            print(f"The list «{self.name}» doesn't have any tasks yet")

    def self_destruct(self):
        del self


