import modules.mini_db as db

# Clase tarea, se almacenan en listas (ToDoList)
class Task:
    def __init__(self, name, is_completed=False, priority=0):
        self.name = name
        self.is_completed = is_completed
        self.priority = priority
    
    def get_task(self):
        return self

    def get_name(self):
        return self.name

    def finish_task(self):
        self.is_completed = True

    def rename(self, new_name):
        self.name = new_name
    
    def prioritize(self, priority: int):
        self.priority = priority

class ToDoList:
    def __init__(self, name, category: str, tasks=list(),
                is_completed=False, priority=0):
        self.name = name
        self.category = category
        self.tasks = tasks
        self.is_completed = is_completed
        db.lists_list.append(self)

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)
        else:
            print('Please provide a valid task')
    
    def print_tasks(self):
        if len(self.tasks) > 0:
            for i, task in enumerate(self.tasks):
                print(f'{i+1}) {task.get_name()}')
        else:
            print('Vaya, no hay tareas!')

    def get_tasks(self):
        return self.tasks

    def get_name(self):
        return self.name


