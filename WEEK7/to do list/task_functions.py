def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            file = f.readlines()
            tasks = []
            for f in file:
                task = {"id":f.split("|")[0], "status":f.split("|")[1], "description":f.split("|")[2]}
                tasks.append(task)
            return tasks
    except FileNotFoundError:
        print("File not found")
        return

def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        for t in tasks:
            task = ""
            for k, v in t.items():
                task += f"{k}|{v}"
            f.writelines(task)

def add_task(filename, description):
    tasks = load_tasks(filename)
    if not tasks:
        last_id = 0
        tasks = []
    else:
        last_id = tasks[-1]["id"]
    tasks.append({"id": last_id+1, "status":"pending", "description": description })
    save_tasks(filename, tasks)

def complete_task(filename, task_id):
    tasks = load_tasks(filename)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            return
    print("task not found")
    return

def list_tasks(filename):
    tasks = load_tasks(filename)
    if not tasks:
        print("no tasks yet")
        return
    for task in tasks:
        print(task)

