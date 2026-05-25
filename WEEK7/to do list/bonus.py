from task_functions import *
def delete_task(filename, task_id):
    tasks = load_tasks(filename)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(filename,tasks)
            print("task removed")
            return
    print("task not found")

def filter(filename, status):
    tasks = load_tasks(filename)
    filterd = []
    for task in tasks:
        if task["status"] == status:
            filterd.append(task)
    return  filterd

def find_task(filename, task_id):
    tasks = load_tasks(filename)
    for task in tasks:
        if task["id"] == task_id:
            return task
    print("task not found")

def statics(filename):
    done = 0
    tasks = load_tasks(filename)
    for task in tasks:
        if task["status"] == 'done':
            done += 1
    print(f"{done} tasks done out of {len(tasks)} tasks")

def is_task(filename, task):
    return task in load_tasks(filename)



