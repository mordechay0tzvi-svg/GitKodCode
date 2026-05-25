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
        return None

def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        f.write(tasks)

def add_task(filename, description):
    tasks = load_tasks(filename)
    last_id = tasks[-1]["id"]
    tasks.append({"id": last_id+1, "status":"pending", "description": description })
    save_tasks(filename, tasks)

